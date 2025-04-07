from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

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



