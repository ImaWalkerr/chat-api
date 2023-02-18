from django.urls import path, include
from src.user_control.views import LoginView, RegisterView, RefreshView


urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('refresh', RefreshView.as_view()),
]
