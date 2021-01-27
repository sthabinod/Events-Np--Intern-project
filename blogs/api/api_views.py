from rest_framework.response import Response
from blogs.api.serializers import UserSerializer
from blogs.api import serializers
from rest_framework import viewsets, permissions
from blogs.models import Blog
from django.contrib.auth.models import User



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer