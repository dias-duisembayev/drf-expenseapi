from rest_framework import permissions
from .models import Category


class IsCategoryOwner(permissions.BasePermission):
    """Permission class to check if user is a category owner"""

    def has_object_permission(self, request, view, obj):
        """Returns True, if the user requesting a category is its owner"""
        if isinstance(obj, Category):
            return obj.owner == request.user
