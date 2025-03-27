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

class RegisterSerializer(serializers.ModelSerializer):  # Inherit from ModelSerializer
    username = serializers.CharField(max_length=150, required=True)  # Explicit CharField
    email = serializers.CharField(max_length=255, required=True)  # Explicit CharField
    password = serializers.CharField(
        max_length=128, 
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )  # Explicit CharField

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        # Ensure explicit use of get_user_model().objects.create_user()
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create token for the user
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)  # Explicit CharField
    password = serializers.CharField(
        max_length=128, 
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )  # Explicit CharField
