from rest_framework import serializers
from src.message_control.models import GenericFileUpload, Message, MessageAttachment


class GenericFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericFileUpload
        fields = '__all__'


class MessageAttachmentSerializer(serializers.ModelSerializer):
    attachment = GenericFileUploadSerializer()

    class Meta:
        models = MessageAttachment
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField('get_sender_data')
    sender_id = serializers.IntegerField(write_only=True)
    receiver = serializers.SerializerMethodField('get_receiver_data')
    receiver_id = serializers.IntegerField(write_only=True)
    message_attachments = MessageAttachmentSerializer(read_only=True, many=True)

    class Meta:
        models = Message
        fields = '__all__'

    def get_sender_data(self, obj):
        from src.user_control.serializers import UserProfileSerializer
        return UserProfileSerializer(obj.sender.user_profile).data

    def get_receiver_data(self, obj):
        from src.user_control.serializers import UserProfileSerializer
        return UserProfileSerializer(obj.sender.user_profile).data
