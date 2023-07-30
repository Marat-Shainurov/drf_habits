from rest_framework.permissions import BasePermission


class IsStaffOrSuperuser(BasePermission):
    message = "You are not permitted to operate with the CustomUser objects!"
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return False