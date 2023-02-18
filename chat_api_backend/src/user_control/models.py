from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


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


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.EmailField(unique=True, max_length=255, verbose_name='Username')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False, verbose_name='Staff status')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser status')
    is_active = models.BooleanField(default=True, verbose_name='Active status')

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Jwt(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='login_user'
    )
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
