from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'website')
    search_fields = ('user__username', 'bio')
    list_filter = ('user',)

