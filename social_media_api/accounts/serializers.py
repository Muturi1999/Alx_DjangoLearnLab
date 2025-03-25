from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Explicitly use CharField for password with validation
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'bio']
        extra_kwargs = {
            'email': {'required': True},
            'bio': {'required': False}
        }

    def validate(self, attrs):
        # Add password confirmation validation
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        # Explicitly use create_user method
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        
        # Create a token for the user
        Token.objects.create(user=user)
        
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']
        read_only_fields = ['id']



class UserFollowSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'bio', 
            'profile_picture', 'followers_count', 
            'following_count', 'is_followed'
        ]
        read_only_fields = ['id', 'username']

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following_users.count()

    def get_is_followed(self, obj):
        # Check if the current user is following this user
        user = self.context['request'].user
        if user.is_authenticated:
            return user.following_users.filter(pk=obj.pk).exists()
        return False