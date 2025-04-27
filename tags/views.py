from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from posts.serializers import PostSerializer
from posts.models import Post
from rest_framework.decorators import action
from rest_framework.response import Response
from categories.permissions import ReadOnly
from .serializers import TagSerializer
from .models import Tag
from .pagination import TagPagination



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination
    permission_classes = [IsAdminUser|ReadOnly]
    lookup_field = 'slug'

    @action(detail=True, methods=['get'], url_path='posts', permission_classes=[IsAdminUser | ReadOnly])
    def posts(self, request, slug=None):
        tag = self.get_object()
        posts = Post.objects.filter(tags=tag)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)