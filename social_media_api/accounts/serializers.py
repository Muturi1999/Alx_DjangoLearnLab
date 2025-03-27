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
    # Explicitly define CharField
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

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