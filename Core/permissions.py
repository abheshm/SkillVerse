from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )
    
class IsTechnician(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and (
                request.user.role == 'technician'
                or request.user.is_superuser
            )
        )
    
class IsCustomer(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and (
                request.user.role == 'customer'
                or request.user.is_superuser
            )
        )