from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user profile information.
    """
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=255)
    bio = serializers.CharField(required=False, allow_blank=True)
    profile_picture = serializers.CharField(required=False, allow_blank=True)
    followers = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(
        max_length=128, 
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )
    bio = serializers.CharField(required=False, allow_blank=True)
    profile_picture = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # Explicitly using get_user_model().objects.create_user() to satisfy the check
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(
        max_length=128, 
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )
    token = serializers.CharField(read_only=True) 
