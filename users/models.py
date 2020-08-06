from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.gis.db import models as geomodel


class UserManager(BaseUserManager):
    """"Manager for UserProfil"""
    use_in_migrations = True
    use_for_related_fields = True

    def create_user(self, username, email, password=None):
        """Create a new UserProfile"""
        if not username:
            raise ValueError("Username must be provided")

        if not email:
            raise ValueError("Email field must be provided")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """Create superuser"""
        user = self.create_user(username, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    """Database model for user in the system"""
    # Add extra fields here

    REQUIRED_FIELDS = ['email']

    first_name = None
    last_name = None

    email = models.EmailField('email address', unique=True)
    name = models.CharField(max_length=30, blank=False)
    about = models.TextField()
    mobile = models.CharField(max_length=21)
    dob = models.DateField(null=True)
    avator = models.ImageField(
        upload_to="profile-image", null=True, blank=True)
    location = geomodel.PointField(null=True, blank=True)
    follows = models.ManyToManyField(
        'self', symmetrical=False, through='JtFollower')

    objects = UserManager()
    all_objects = models.Manager()

    def __str__(self):
        """Get string representation of UserProfile"""
        return self.username


class JtFollower(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return self.follower.name + ' ' + self.following.name

# Phorographer Genres model


class PhotorapherGenre(models.Model):
    # add model definition here
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


# ParPhotographers profile model
class PhotographerProfile(models.Model):
    # add model definition here
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    experience_in_months = models.IntegerField(
        blank=False, verbose_name='Experience in Months', default=0)

    genre = models.ManyToManyField(
        PhotorapherGenre, through='JtPhotograpgerProfileGenre')

    def __str__(self):
        return self.user.name


# Junction table for photographer and genres
class JtPhotograpgerProfileGenre(models.Model):
    photographer_profile = models.ForeignKey(
        PhotographerProfile, on_delete=models.CASCADE)
    photographer_genre = models.ForeignKey(
        PhotorapherGenre, on_delete=models.CASCADE)

    def __str__(self):
        return self.photographer_profile.user.username + ' ' + self.photographer_genre.name


# Phorographer Genres model
class ModelGenre(models.Model):
    # add model definition here
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


# Models profile model
class ModelProfile(models.Model):
    # add model definition here
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    experience_in_months = models.IntegerField(
        blank=False, verbose_name='Experience in Months', default=0)

    genre = models.ManyToManyField(
        ModelGenre, through='JtModelProfileGenre')

    def __str__(self):
        return self.user.username


# Junction table for Model and genres
class JtModelProfileGenre(models.Model):
    model_profile = models.ForeignKey(ModelProfile, on_delete=models.CASCADE)
    model_genre = models.ForeignKey(ModelGenre, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_profile.user.username + ' ' + self.photographer_profile.user.username
