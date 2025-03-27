from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)  # Explicitly define CharField
    email = serializers.CharField(max_length=255, required=True)  # Explicitly define CharField
    password = serializers.CharField(write_only=True, required=True)  # Explicitly define CharField

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract password separately
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Ensure password is hashed
        user.save()
        Token.objects.create(user=user)
        return user
