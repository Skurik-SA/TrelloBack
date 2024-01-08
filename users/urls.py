from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from boards.views import DashboardAPIView
from .views import RegistrationAPIView, ProfileAPIView, CustomTokenObtainPairView, LogoutAPIView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('boards/', DashboardAPIView.as_view(), name='dashboards')
    # path('profile/<uuid:user>', ProfileAPIView.as_view(), name='get_profile'),
    # path('profile/<int:pk>', ProfileAPIView.as_view(), name='get_profile'),
]