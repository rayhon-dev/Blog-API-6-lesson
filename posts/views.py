from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from .pagination import PostPagination
from rest_framework.permissions import IsAdminUser
from .permissions import ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAdminUser | ReadOnly]
    lookup_field = 'slug'
