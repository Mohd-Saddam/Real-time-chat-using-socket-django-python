from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication
from channels.middleware import BaseMiddleware


@database_sync_to_async
def get_user(token):
    try:
        authentication = JWTAuthentication()
        validated_token = authentication.get_validated_token(token)
        user = authentication.get_user(validated_token)
        return user
    except:
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        query_string = scope['query_string'].decode()
        token_key = None
        for param in query_string.split('&'):
            key, value = param.split('=')
            if key == 'token':
                token_key = value.strip("Bearer ")

        scope['user'] = await get_user(token_key)

        return await super().__call__(scope, receive, send)
