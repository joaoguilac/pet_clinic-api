from rest_framework import permissions
from django.contrib.auth import get_user_model

from PetClinicAPI.apps.authentication.models import User

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
                return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role == User.RoleChoices.ADMIN

class IsVetOrAdminOrReadOnly(permissions.BasePermission):
    
        def has_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:
                return True

            if not request.user.is_authenticated:
                return False

            if request.user.role == User.RoleChoices.ADMIN:
                return True

            return request.user.role == User.RoleChoices.VET
