from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'bio',
            'profile_picture',
            'website'
        ]


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    def create(self, validation_data):
        return User.objects.create_user(**validation_data)







# {
#   "username": "newuser",
#   "email": "newuser@example.com",
#   "password": "securepassword123",
#   "password2": "securepassword123",
#   "first_name": "New",
#   "last_name": "User"
# }