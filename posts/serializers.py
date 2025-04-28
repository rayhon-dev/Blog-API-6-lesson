from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from postlikes.models import PostLike
from categories.models import Category
from tags.models import Tag


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class PostTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = PostCategorySerializer(read_only=True)
    tags = PostTagsSerializer(many=True, read_only=True)

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



class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'user', 'value', 'created_at']
        read_only_fields = ['id', 'post', 'user', 'created_at']

    def create(self, validated_data):
        post = self.context['post']
        user = self.context['request'].user
        value = validated_data.get('value')

        like, created = PostLike.objects.get_or_create(
            post=post,
            user=user,
            defaults={'value': value}
        )
        if not created:
            like.value = value
            like.save()

        return like
