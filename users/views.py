from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import Profile, CustomUser
from users.serializers import RegistrationSerializer, CustomUserSerializer, CustomTokenObtainPairSerializer, \
    ProfileSerializer, LogoutSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Create your views here.


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=HTTP_204_NO_CONTENT)


class ProfileAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            uuid = request.data['uuid']
            profile = self.queryset.get(user=uuid)
            serialized_data = ProfileSerializer(profile).data
            return Response(data=serialized_data, status=HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found for the specified user"}, status=HTTP_404_NOT_FOUND)
