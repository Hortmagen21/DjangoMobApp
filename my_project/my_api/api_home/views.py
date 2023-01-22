import my_auth.models as auth_models
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ProfileSerializer
from rest_framework import permissions


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = auth_models.Profile.objects.all()
    serializer_class = ProfileSerializer




