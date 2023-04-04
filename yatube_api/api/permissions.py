from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        del view
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        del view
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
