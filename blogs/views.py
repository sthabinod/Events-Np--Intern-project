from rest_framework.response import Response
from blogs.api.serializers import UserSerializer, BlogSerializer
from blogs.api import serializers
from rest_framework import viewsets, permissions
from blogs.models import Blog
from django.contrib.auth.models import User
from blogs.permissions import BlogPermission


# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        BlogPermission
                        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)