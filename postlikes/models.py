from django.db import models
from posts.models import Post
from django.contrib.auth.models import User


class PostLike(models.Model):
    VALUE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike')
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.CharField(choices=VALUE_CHOICES)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.value} - {self.post.title}"

