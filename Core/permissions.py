from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
    
class IsTechnician(BasePermission):
    def has_permission (self, request, view):
        return request.user.is_authenticated and (
            request.user.role -- 'technician' or request.user.role == 'admin'
        )
    
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'customer' or request.user.role == 'admin'
        )