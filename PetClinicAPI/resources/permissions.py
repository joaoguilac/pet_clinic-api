from rest_framework import permissions
from django.contrib.auth import get_user_model

from PetClinicAPI.apps.authentication.models import User

class IsAdminForRegisterAndIsOwnerToEdit(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated) and bool(request.user.role == User.RoleChoices.ADMIN)

    def has_object_permission(self, request, view, obj) -> bool:
        if not request.user.is_authenticated:
            return False

        if request.user.role == User.RoleChoices.ADMIN:
            return True

        if request.method == 'POST':
            return False

        if request.data.get('role'):
            if request.data.get('role') == User.RoleChoices.ADMIN:
                return False

            if request.data.get('role') == User.RoleChoices.VETERINARY:
                return False

            if request.data.get('role') == User.RoleChoices.OPERATOR:
                return bool(request.user.role == User.RoleChoices.VETERINARY and request.user.id == obj.id)

        return bool(obj == request.user)


class IsVetOrAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view) -> bool:
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user.role == User.RoleChoices.ADMIN or request.user.role == User.RoleChoices.VETERINARY)

class IsVeterinartOrIsAuthenticatedReadOnly(permissions.BasePermission):

    def has_permission(self, request, view) -> bool:
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user.role == User.RoleChoices.VETERINARY)