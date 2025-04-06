from django.contrib import admin
from .models import PostLike

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'value', 'created_at')
    list_filter = ('value', 'created_at')
    search_fields = ('post__title', 'user__username')
    ordering = ('-created_at',)
