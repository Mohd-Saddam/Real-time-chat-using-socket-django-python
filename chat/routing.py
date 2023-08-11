from django.urls import re_path 
from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
# ]

websocket_urlpatterns = [
    re_path(r'ws/socket-server/(?P<user_id>\w+)/$', consumers.ChatConsumer.as_asgi())
]
