from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from .pagination import PostPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrAdminOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    lookup_field = 'slug'
