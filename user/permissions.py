from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        print('request.user: ', request.user.is_staff)
        
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )

class IsStaffAutherization(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        print('request.user: ', request.user.is_staff)
        
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )

class IsSuperUserAutherization(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        print('request.user: ', request.user.is_staff)
        
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_admin
        )