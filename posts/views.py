from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from .pagination import PostPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrAdminOrReadOnly
from django.contrib.auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], url_path='users/(?P<username>[^/.]+)')  # Custom route
    def user_posts(self, request, username=None):
        try:
            user = User.objects.get(username=username)  # Foydalanuvchini olish
            posts = Post.objects.filter(author=user)  # Foydalanuvchining postlarini olish
            page = self.paginate_queryset(posts)  # Sahifalash
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(posts, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)