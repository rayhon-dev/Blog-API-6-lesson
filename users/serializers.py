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




class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']

        extra_kwargs = {
            'username': {'read_only': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def get_profile(self, instance):
        try:
            profile = instance.profile
            return {
                "bio": profile.bio,
                "profile_picture": profile.profile_picture.url if profile.profile_picture else None,
                "website": profile.website
            }
        except UserProfile.DoesNotExist:
            return {
                "bio": "",
                "profile_picture": None,
                "website": ""
            }



    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile, created = UserProfile.objects.get_or_create(user=instance)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.profile_picture = profile_data.get('profile_picture', profile.profile_picture)
        profile.save()

        return instance

class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()



    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


