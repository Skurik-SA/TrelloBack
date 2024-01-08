from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from boards.views import DashboardAPIView

urlpatterns = [
    path('boards/', DashboardAPIView.as_view(), name='dashboards')
]