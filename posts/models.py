from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from categories.models import Category
from tags.models import Tag


class Post(models.Model):
    STATUS_CHOICES = [
        ('df', 'Draft'),
        ('pb', 'Published')
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    featured_image = models.ImageField(upload_to='post_images', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
