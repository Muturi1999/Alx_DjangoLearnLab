from rest_framework import viewsets, generics, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk']).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    """
    Retrieve posts from users the authenticated user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following_users.all()  
        return Post.objects.filter(author__in=following_users).order_by('-created_at') 


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk): 
        post = generics.get_object_or_404(Post, pk=pk) 
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'message': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )

        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):  
        post = generics.get_object_or_404(Post, pk=pk) 
        like = Like.objects.filter(user=request.user, post=post)

        if not like.exists():
            return Response({'message': 'Not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
