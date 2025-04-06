from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'slug'
        ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }