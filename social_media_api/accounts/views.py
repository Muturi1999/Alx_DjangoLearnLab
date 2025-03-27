# from django.contrib.auth import authenticate
# from rest_framework import generics, status, permissions
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView
# from django.contrib.auth import get_user_model


# from .models import CustomUser
# from .serializers import UserSerializer, RegisterSerializer
# User = get_user_model()


# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         user = CustomUser.objects.get(username=response.data['username'])
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'user': response.data}, status=status.HTTP_201_CREATED)

# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)

#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

# class FollowUserView(APIView):
#     """Allow authenticated users to follow another user."""
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, user_id):
#         try:
#             user_to_follow = User.objects.get(id=user_id)
#             request.user.follow(user_to_follow)
#             return Response({'message': 'User followed successfully'}, status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# class UnfollowUserView(APIView):
#     """Allow authenticated users to unfollow another user."""
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, user_id):
#         try:
#             user_to_unfollow = User.objects.get(id=user_id)
#             request.user.unfollow(user_to_unfollow)
#             return Response({'message': 'User unfollowed successfully'}, status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(generics.GenericAPIView):
    """Allow authenticated users to follow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)

        if request.user == user_to_follow:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)  # Assuming 'following' is a ManyToManyField
        return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """Allow authenticated users to unfollow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)

        if request.user == user_to_unfollow:
            return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)  
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
