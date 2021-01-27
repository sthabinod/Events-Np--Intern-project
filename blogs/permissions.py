from rest_framework import permissions

class BlogPermission(permissions.BasePermission):

    def object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user