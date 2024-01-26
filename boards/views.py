from django.shortcuts import render
from rest_framework import generics, permissions

from boards.models import Dashboard
from boards.serializers import DashboardSerializer


# Create your views here.
# Path: boards/models.py
class DashboardAPIView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dashboard.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


