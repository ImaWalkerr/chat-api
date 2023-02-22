from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from src.core.abstract_field import BaseModel
from src.core.enums import GenderTypes
from src.message_control.models import GenericFileUpload


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Username field is required')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have superuser=True')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser, BaseModel, PermissionsMixin):
    username = models.EmailField(unique=True, max_length=255, verbose_name='Username')
    is_staff = models.BooleanField(default=False, verbose_name='Staff status')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser status')
    is_online = models.DateTimeField(default=timezone.now, verbose_name='Online status')

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_control_customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['id']


class UserProfile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(max_length=255, verbose_name='User first name')
    last_name = models.CharField(max_length=255, verbose_name='User last name')
    avatar = models.ForeignKey(
        GenericFileUpload,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_avatar',
        verbose_name='User avatar'
    )
    birthday = models.DateField()
    gender = models.CharField(choices=GenderTypes.choices(), max_length=6, verbose_name='User gender')
    phone = models.CharField(max_length=32, null=True, blank=True, verbose_name='User phone')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='User address')
    number = models.CharField(max_length=32, null=True, blank=True, verbose_name='User address number')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='User city')
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name='User country')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_control_user_profile'
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'
        ordering = ['id']


class Jwt(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='login_user')
    access = models.TextField()
    refresh = models.TextField()

    class Meta:
        db_table = 'user_control_jwt'
        verbose_name = 'Jwt'
        ordering = ['id']
