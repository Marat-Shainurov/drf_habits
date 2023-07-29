from rest_framework import generics

from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomUserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class CustomUserListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class CustomUserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class CustomUserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
