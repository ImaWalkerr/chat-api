from django.urls import path, include
from rest_framework.routers import DefaultRouter
from src.user_control.views import (
    LoginView,
    RegisterView,
    RefreshView,
    UserProfileView,
)


router = DefaultRouter(trailing_slash=False)

router.register(r'profile', UserProfileView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('refresh', RefreshView.as_view()),
]
