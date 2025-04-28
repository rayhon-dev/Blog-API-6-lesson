from rest_framework import serializers



class PostLikesSerializer(serializers.Serializer):
    value = serializers.ChoiceField(choices=['like', 'dislike'])

