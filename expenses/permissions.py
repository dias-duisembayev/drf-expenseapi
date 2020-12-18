from rest_framework import permissions
from .models import Category


class IsCategoryOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Category):
            return obj.owner == request.user
