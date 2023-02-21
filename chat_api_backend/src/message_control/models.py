from django.db import models
from src.core.abstract_field import BaseModel


class GenericFileUpload(BaseModel):
    file_upload = models.ImageField(upload_to='media/avatar/', null=True, blank=True)

    def __str__(self):
        return f'{self.file_upload}'

    class Meta:
        db_table = 'message_control_gen_file_upload'
        verbose_name = 'Generic file upload'
        ordering = ['id']


class Message(BaseModel):
    sender = models.ForeignKey(
        to='user_control.CustomUser',
        on_delete=models.CASCADE,
        related_name='message_sender',
        verbose_name='Message sender'
    )
    receiver = models.ForeignKey(
        to='user_control.CustomUser',
        on_delete=models.CASCADE,
        related_name='message_receiver',
        verbose_name='Message receiver'
    )
    message = models.TextField(null=True, blank=True, verbose_name='Message')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'message between {self.sender.username} and {self.receiver.username}'

    class Meta:
        db_table = 'message_control_message_table'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['id']


class MessageAttachment(BaseModel):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='message_attachments',
        verbose_name='Message attachments'
    )
    attachment = models.ForeignKey(
        GenericFileUpload,
        on_delete=models.CASCADE,
        related_name='message_uploads',
        verbose_name='Message uploads'
    )
    caption = models.CharField(max_length=255, null=True, blank=True, verbose_name='Message caption')

    class Meta:
        db_table = 'message_control_message_attachments'
        verbose_name = 'Message attachment'
        verbose_name_plural = 'Message attachments'
        ordering = ['id']
