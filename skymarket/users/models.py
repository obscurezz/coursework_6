from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles(models.TextChoices):
    ADMIN = 'admin'
    USER = 'user'


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = PhoneNumberField(max_length=20, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='users/', null=True)
    is_active = models.BooleanField(null=False, default=True)

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

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

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['email']

    def __str__(self):
        return f'{self.email}, {self.phone}'
