from rest_framework import serializers
from .models import Comment


class PostCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    slug = serializers.SlugField()

class AuthorCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    post = PostCommentSerializer(read_only=True)
    author = AuthorCommentSerializer(read_only=True)
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'content',
            'created_at',
            'parent'
        ]

    def get_parent(self, obj):
        return obj.parent.id if obj.parent else None
