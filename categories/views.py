from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
from .pagination import CategoryPagination



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    lookup_field = 'pk'



