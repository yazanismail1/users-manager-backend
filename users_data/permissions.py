from rest_framework.permissions import BasePermission, SAFE_METHODS

class OwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else: return False
