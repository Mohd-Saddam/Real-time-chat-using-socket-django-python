from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework import generics
from account.models import User
from account.serializers import UserResponseSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')


# Create your views here.
class FindUsersToConnect(generics.ListAPIView):
    serializer_class = UserResponseSerializer
    queryset = User.objects.filter(is_online=True)
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = request.user
        user_interests = user.interests.all()
        queryset = self.queryset.exclude(id=user.id)

        # Find users with same interest
        final_queryset = queryset.filter(interests__in=user_interests)

        if not final_queryset:
            final_queryset = queryset

        serializer = self.get_serializer(final_queryset, many=True)

        return JsonResponse(serializer.data, status=200)
