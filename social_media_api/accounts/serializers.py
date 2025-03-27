# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from rest_framework.authtoken.models import Token

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')

# class RegisterSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=150, required=True)  # Explicitly define CharField
#     email = serializers.CharField(max_length=255, required=True)  # Explicitly define CharField
#     password = serializers.CharField(write_only=True, required=True)  # Explicitly define CharField

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password')  # Extract password separately
#         user = User.objects.create_user(**validated_data)
#         user.set_password(password)  # Ensure password is hashed
#         user.save()
#         Token.objects.create(user=user)
#         return user
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
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration with explicit CharField definitions.
    """
    # Explicitly define CharField with validation
    username = serializers.CharField(
        max_length=150, 
        required=True, 
        help_text="Enter a unique username"
    )
    email = serializers.EmailField(
        max_length=255, 
        required=True, 
        help_text="Enter a valid email address"
    )
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        min_length=8,
        help_text="Enter a strong password (min 8 characters)"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Create and return a new user instance, 
        creating an authentication token in the process.
        """
        # Extract password separately
        password = validated_data.pop('password')
        
        # Create user using create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            **validated_data
        )
        
        # Set password securely
        user.set_password(password)
        user.save()
        
        # Create authentication token for the user
        Token.objects.create(user=user)
        
        return user

    def validate_username(self, value):
        """
        Additional username validation
        """
        # Check if username already exists
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def validate_email(self, value):
        """
        Additional email validation
        """
        # Check if email already exists
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value