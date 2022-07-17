from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    ROLES = [('user', 'Пользователь'), ('admin', 'Админ')]
    ADMIN = 'admin'
    USER = 'user'


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = PhoneNumberField()
    role = models.CharField(max_length=9, choices=UserRoles.ROLES, default='user')
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
