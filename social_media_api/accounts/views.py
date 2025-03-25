from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserFollowSerializer

User = get_user_model()

from .serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer, 
    UserProfileSerializer
)

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Get or create token
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'user': UserProfileSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user:
            # Get or create token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserProfileSerializer(user).data
            })
        
        return Response(
            {'error': 'Invalid Credentials'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

class UserProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(
            request.user, 
            data=request.data, 
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
    


class FollowUserView(APIView):
    """
    View to handle following and unfollowing users
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        """
        Follow a user
        """
        target_user = get_object_or_404(User, pk=user_id)
        
        # Prevent following self
        if target_user == request.user:
            return Response(
                {'error': 'You cannot follow yourself'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Add to following
        request.user.follow(target_user)
        
        serializer = UserFollowSerializer(
            target_user, 
            context={'request': request}
        )
        return Response(serializer.data)

class UnfollowUserView(APIView):
    """
    View to unfollow a user
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        """
        Unfollow a user
        """
        target_user = get_object_or_404(User, pk=user_id)
        
        # Remove from following
        request.user.unfollow(target_user)
        
        serializer = UserFollowSerializer(
            target_user, 
            context={'request': request}
        )
        return Response(serializer.data)

class UserFollowersListView(generics.ListAPIView):
    """
    View to list a user's followers
    """
    serializer_class = UserFollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        return user.followers.all()

class UserFollowingListView(generics.ListAPIView):
    """
    View to list users a user is following
    """
    serializer_class = UserFollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        return user.following_users.all()