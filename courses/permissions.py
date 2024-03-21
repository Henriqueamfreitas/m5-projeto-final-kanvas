from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Course


class IsSuperUserOrOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Course):
        return request.user.is_superuser or request.user == obj.instructor