from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS for everyone
        if request.method in SAFE_METHODS:
            return True
        
        # Allow POST/PUT/DELETE only for admin
        return request.user and request.user.is_staff
    
    
class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view): 
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == 'GET' or admin_permission
    
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user