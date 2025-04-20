from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/register/', views.UserCreateView.as_view(), name='user-create'),
    path('auth/login/', TokenObtainPairView.as_view(), name='user-login')

]