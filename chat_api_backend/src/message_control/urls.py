from rest_framework.routers import DefaultRouter
from src.message_control.views import GenericFileUploadView, MessageView
from django.urls import path, include


router = DefaultRouter(trailing_slash=False)

router.register(r'file-upload', GenericFileUploadView, basename='file-upload')
router.register(r'message', MessageView, basename='message')

url_patterns = [
    path('', include(router.urls))
]
