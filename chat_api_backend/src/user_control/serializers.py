from django.db.models import Q
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
    message_count = serializers.SerializerMethodField('get_message_count')

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_message_count(self, obj):
        try:
            user_id = self.context['request'].user.id
        except Exception as e:
            user_id = None

        from src.message_control.models import Message
        message = Message.objects.filter(Q(sender_id=user_id, receiver=obj.user.id) |
                                         Q(sender_id=obj.user.id, receiver=user_id)).distinct()
        return message.count()
