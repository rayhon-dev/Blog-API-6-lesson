from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from .pagination import CommentPagination
from rest_framework.permissions import IsAdminUser
from .permissions import ReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    permission_classes = [IsAdminUser | ReadOnly]
    lookup_field = 'slug'
