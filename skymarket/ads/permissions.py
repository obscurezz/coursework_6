from rest_framework import permissions
from users.models import UserRoles


class UserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action == 'retrieve':
            return True
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user or request.user.role == UserRoles.ADMIN
        else:
            return False
