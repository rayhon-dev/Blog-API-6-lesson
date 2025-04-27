from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
from .pagination import CategoryPagination
from rest_framework.permissions import IsAdminUser
from .permissions import ReadOnly
from posts.serializers import PostSerializer
from posts.models import Post
from rest_framework.decorators import action
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAdminUser | ReadOnly]
    lookup_field = 'slug'

    @action(detail=True, methods=['get'], url_path='posts', permission_classes=[IsAdminUser | ReadOnly])
    def posts(self, request, slug=None):
        category = self.get_object()
        posts = Post.objects.filter(category=category)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
