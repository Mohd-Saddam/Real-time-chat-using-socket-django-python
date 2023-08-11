from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)
    country = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'password', 'full_name', 'email', 'phone', 'gender', 'country')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        email = validated_data.pop('email')
        phone = validated_data.pop('phone')
        gender = validated_data.pop('gender')
        country = validated_data.pop('country')

        user = User.objects.create_user(
            username=email,
            password=validated_data['password']
        )

        user.full_name = full_name
        user.email = email
        user.phone = phone
        user.gender = gender
        user.country = country

        user.save()

        return user


class InterestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class UserResponseSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'email', 'phone', 'gender', 'country', 'is_online', 'interests')

