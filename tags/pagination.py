from rest_framework.pagination import PageNumberPagination


class TagPagination(PageNumberPagination):
    page_size = 5