from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import exception_handler


class IsAuthenticatedCustom(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            from src.user_control.models import CustomUser
            CustomUser.objects.filter(id=request.user.id).update(is_online=timezone.now())
            return True
        return False


class IsAuthenticatedOrReadCustom(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated:
            from src.user_control.models import CustomUser
            CustomUser.objects.filter(id=request.user.id).update(is_online=timezone.now())
            return True
        return False


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        return response

    exc_line = str(exc).split('DETAIL: ')
    return Response({'error': exc_line[-1]}, status=status.HTTP_403_FORBIDDEN)
