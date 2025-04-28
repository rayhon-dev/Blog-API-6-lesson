from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, PostLikeSerializer
from .pagination import PostPagination
from .permissions import IsOwnerOrAdminOrReadOnly

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], url_path='like', permission_classes=[IsAuthenticated])
    def like_post(self, request, slug=None):

        post = self.get_object()

        serializer = PostLikeSerializer(
            data=request.data,
            context={'post': post, 'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPostListView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise NotFound('User not found.')
        return Post.objects.filter(author=user)
