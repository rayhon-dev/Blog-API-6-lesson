from django.urls import path
from .views import  CommentDetail

urlpatterns = [
    path('comments/<int:id>/', CommentDetail.as_view(), name='comment-detail'),
]