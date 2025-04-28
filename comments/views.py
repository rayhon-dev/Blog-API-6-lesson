from rest_framework import generics, permissions
from .models import Comment
from posts.models import Post
from .pagination import CommentPagination
from .serializers import CommentSerializer, CommentCreateSerializer
from .permissions import IsAuthenticatedOrReadOnly, IsCommentAuthorOrPostAuthorOrAdminOrReadOnly


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CommentPagination

    def get_queryset(self):
        post_slug = self.kwargs['slug']
        return Comment.objects.filter(post__slug=post_slug)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        post_slug = self.kwargs['slug']
        post = Post.objects.get(slug=post_slug)
        serializer.save(author=self.request.user, post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrPostAuthorOrAdminOrReadOnly]
    lookup_url_kwarg = 'id'