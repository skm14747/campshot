from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from users.models import *
# Register your models here.


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {
         'fields': ('name', 'mobile', 'email', 'dob', 'avator', 'location')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff',
                                      'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'name', 'groups'),
        }),
    )
    list_display = ('username', 'email', 'name')
    search_fields = ('username', 'email', 'name')
    ordering = ('username', 'email', 'name')


admin.site.register(JtFollower)
admin.site.register(PhotographerProfile)
admin.site.register(PhotorapherGenre)
admin.site.register(JtPhotograpgerProfileGenre)
admin.site.register(ModelProfile)
admin.site.register(ModelGenre)
admin.site.register(JtModelProfileGenre)
