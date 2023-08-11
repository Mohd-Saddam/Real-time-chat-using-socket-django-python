import json
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserResponseSerializer
from .models import User, Interest


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is None:
            user = User.objects.filter(phone=username).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        data = [{"id":user.id,
            "email":user.email,
            "phone":user.phone,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "messgae":"User login successfully"}]
        return Response({
            "data":data
        },status=status.HTTP_200_OK)


class UpdateUserInterest(generics.UpdateAPIView):
    serializer_class = UserResponseSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        add_interests = request.data.get('add_interests', [])
        remove_interests = request.data.get('remove_interests', [])
        user = request.user

        for interest_name in add_interests:
            interest, is_created = Interest.objects.get_or_create(name=interest_name)
            user.interests.add(interest)

        for interest_name in remove_interests:
            interest = Interest.objects.filter(name=interest_name).first()
            if interest:
                user.interests.remove(interest)

        serializer = self.get_serializer(user)

        return JsonResponse(serializer.data, status=200)


class UpdateUserActiveStatus(generics.UpdateAPIView):
    serializer_class = UserResponseSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = request.user
        user.is_online = not user.is_online
        user.save()

        serializer = self.get_serializer(user)

        return JsonResponse(serializer.data, status=200)
