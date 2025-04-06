from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'slug'
        ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }