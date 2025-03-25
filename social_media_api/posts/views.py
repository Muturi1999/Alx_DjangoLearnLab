from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, permissions


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    # Filtering and Search
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    filterset_fields = ['author__username']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'likes']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    # Filtering
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter
    ]
    filterset_fields = ['post', 'author__username']
    search_fields = ['content']

    def get_queryset(self):
        # Option to filter comments by post
        post_id = self.request.query_params.get('post', None)
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



# class UserFeedView(generics.ListAPIView):
#     """
#     View to retrieve a user's feed (posts from followed users)
#     """
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         # Get users that the current user is following
#         following_users = self.request.user.following_users.all()
        
#         # Return posts from followed users, ordered by most recent
#         return Post.objects.filter(
#             author__in=following_users
#         ).order_by('-created_at')
    
class UserFeedView(generics.ListAPIView):
    """
    View to retrieve a user's feed (posts from followed users)
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get users that the current user is following
        following_users = self.request.user.following_users.all()
        
        # Return posts from followed users, ordered by most recent
        return Post.objects.filter(
            author__in=following_users
        ).order_by('-created_at')