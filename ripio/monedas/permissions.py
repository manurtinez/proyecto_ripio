from rest_framework import permissions


class BasicUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Acciones abiertas excepto transfer_to_user
        if view.action != 'transfer_to_user':
            return True
        if view.action == 'transfer_to_user' and request.user.is_authenticated:
            return True
        return False
