from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        del view
        return (request.method in permissions.SAFE_METHODS or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        del view
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.autor == request.user