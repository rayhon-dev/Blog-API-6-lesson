from rest_framework import pagination


class CategoryPagination(pagination.PageNumberPagination):
    page_size = 5