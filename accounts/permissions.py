from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    
    
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return getattr(user, 'role', None) == 'admin' or user.is_staff or user.is_superuser

class IsOwnerOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return obj == request.user
        return obj == request.user
