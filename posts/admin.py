from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'category', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)  # Makes tag selection easier
