import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.models import User
from chat.models import Room, Conversation, Message


def get_user(token):
    try:
        authentication = JWTAuthentication()
        validated_token = authentication.get_validated_token(token)
        user = authentication.get_user(validated_token)
        return user
    except:
        return None


class ChatConsumer(WebsocketConsumer):

    def extract_users_info(self):
        headers = self.scope['headers']
        authorization_header = next((value for name, value in headers if name == b'authorization'), None)

        if authorization_header:
            authorization_value = authorization_header.decode().split(' ')[1]
            initiator = get_user(authorization_value)
            if not initiator:
                return None, None
        else:
            return None, None

        receiver_user_id = self.scope['url_route']['kwargs']['user_id']
        receiver = User.objects.filter(id=receiver_user_id).first()

        return initiator, receiver

    def find_room(self, current_user, connect_to_user):

        room = Room.objects.filter(
            Q(participant_1=current_user, participant_2=connect_to_user) |
            Q(participant_1=connect_to_user, participant_2=current_user)
        ).first()

        if not room:
            print("room not found")
            room = Room.objects.create(
                participant_1=current_user,
                participant_2=connect_to_user
            )
        print(room.id)
        return room

    def connect(self):
        initiator, receiver = self.extract_users_info()

        if not initiator or not receiver:
            return None

        self.room_group_name = f"{self.find_room(initiator, receiver).id}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        initiator, receiver = self.extract_users_info()
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

        conversation = Conversation.objects.create(
            initiator=initiator,
            receiver=receiver
        )

        Message.objects.create(
            sender=initiator,
            text=message,
            conversation=conversation
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
