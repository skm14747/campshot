from django.db import models
from django.contrib.gis.db import models as geomodel
from users.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_picture = models.ImageField(
        upload_to="post_picture", null=False, blank=False)
    caption = models.TextField(blank=True)
    location = geomodel.PointField(null=True, blank=True)
    is_private = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Comment(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = TreeForeignKey('self', on_delete=models.CASCADE,
                                    null=True, blank=True, related_name='child_comment')
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
