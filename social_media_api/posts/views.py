# from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework import permissions

# from .models import Post, Comment
# from .serializers import PostSerializer, CommentSerializer
# from django_filters.rest_framework import DjangoFilterBackend


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('-created_at')
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'content']

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all() 
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         return Comment.objects.filter(post_id=self.kwargs['post_pk']).order_by('-created_at')

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class UserFeedView(generics.ListAPIView):
#     """
#     Retrieve posts from users the authenticated user follows.
#     """
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Post.objects.filter(author__in=user.following.all()).order_by('-created_at')

from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


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
