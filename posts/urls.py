from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from comments.views import CommentList

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<str:username>/posts/', views.UserPostListView.as_view(), name='user-posts'),
    path('posts/<slug:slug>/comments/', CommentList.as_view(), name='post-comments'),
]

