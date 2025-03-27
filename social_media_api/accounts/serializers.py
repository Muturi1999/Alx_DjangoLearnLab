from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user profile information.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.Serializer):
    # Explicitly use CharField for each field
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        max_length=128, 
        write_only=True, 
        style={'input_type': 'password'}
    )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create token for the user
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    # Additional serializer for login with explicit CharField
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        max_length=128, 
        style={'input_type': 'password'}
    )