from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/register/', views.UserCreateView.as_view(), name='user-create'),
    path('auth/login/', TokenObtainPairView.as_view(), name='user-login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='user-token-refresh'),
    path('auth/logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('users/me/', views.CurrentUserView.as_view(), name='my-profile'),
    path('users/<str:username>/', views.UserProfileView.as_view(), name='user-profile'),
]
