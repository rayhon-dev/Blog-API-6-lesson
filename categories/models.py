from django.db import models
from django.utils.text import slugify
from random import randint




class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.name)}-{randint(1, 1000)}"
        super().save(*args, **kwargs)

