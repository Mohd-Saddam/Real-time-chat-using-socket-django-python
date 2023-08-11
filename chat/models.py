from django.db import models
from django.conf import settings

from utils.models import TimeStampedModel


# Create your models here.

class Conversation(TimeStampedModel):
    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="convo_starter", null=True
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="convo_participant", null=True
    )
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Conversation between {self.initiator.username} and {self.receiver.username}'


class Message(TimeStampedModel):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='message_sender', null=True)
    text = models.CharField(max_length=200)
    attachment = models.FileField(null=True, blank=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_on',)


class Room(TimeStampedModel):
    participant_1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='room_participant_1')
    participant_2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='room_participant_2')

    def __str__(self):
        return f'Room {self.id}'
