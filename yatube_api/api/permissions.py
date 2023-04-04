from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Проверяет на аутентификацию и авторство, если небезопасный метод."""
    def has_permission(self, request, view) -> bool:
        del view
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj) -> bool:
        del view
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
