from django.shortcuts import render
from rest_framework import generics, permissions

from boards.models import Dashboard
from boards.serializers import DashboardSerializer


# Create your views here.

class DashboardAPIView(generics.CreateAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]
