from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')

class PostAuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

class PostCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)

class PostTagsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)




class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'content',
            'author',
            'category',
            'tags',
            'created_at',
            'updated_at',
            'status',
            'featured_image',
        )
        extra_kwargs = {
            'slug': {'read_only': True},
            'author': {'read_only': True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = PostAuthorSerializer(instance.author).data
        data['category'] = PostCategorySerializer(instance.category).data
        data['tags'] = PostTagsSerializer(instance.tags.all(), many=True).data
        return data

