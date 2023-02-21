from rest_framework import serializers
from src.user_control.models import CustomUser, UserProfile
from src.message_control.serializers import GenericFileUploadSerializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class CustomUserSerializer(serializers.Serializer):

    class Meta:
        model = CustomUser
        exclude = ('password', )


class UserProfileSerializer(serializers.Serializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    avatar = GenericFileUploadSerializer(read_only=True)
    avatar_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = UserProfile
        fields = '__all__'
