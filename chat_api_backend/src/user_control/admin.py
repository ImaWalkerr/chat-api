from django.contrib import admin
from src.user_control.models import CustomUser, Jwt


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Jwt)
class JwtAdmin(admin.ModelAdmin):
    pass
