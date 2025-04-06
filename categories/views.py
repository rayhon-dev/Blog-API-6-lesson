from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
from .pagination import CategoryPagination
from rest_framework.permissions import IsAdminUser
from .permissions import ReadOnly



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAdminUser | ReadOnly]
    lookup_field = 'slug'


