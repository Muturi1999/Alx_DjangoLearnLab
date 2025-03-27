from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user profile information.
    """
    # Explicitly add CharField for demonstration
    username = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.Serializer):
    # Explicitly define CharField with detailed parameters
    username = serializers.CharField(
        max_length=150, 
        required=True, 
        error_messages={
            'required': 'Username is required',
            'max_length': 'Username must be at most 150 characters'
        }
    )
    email = serializers.CharField(
        max_length=255, 
        required=True, 
        error_messages={
            'required': 'Email is required',
            'max_length': 'Email must be at most 255 characters'
        }
    )
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        min_length=8,
        error_messages={
            'required': 'Password is required',
            'min_length': 'Password must be at least 8 characters'
        }
    )

    def create(self, validated_data):
        # Use get_user_model().objects.create_user explicitly
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        # Create token for the user
        Token.objects.create(user=user)
        
        return user