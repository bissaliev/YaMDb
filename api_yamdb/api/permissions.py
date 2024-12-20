from rest_framework import permissions


class IsAdminOrSuperuser(permissions.BasePermission):
    """Доступ только для админов или суперюзеров."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class ISAdminOnlyEdit(permissions.BasePermission):
    """Просмотр доступен всем пользователям, изменение только администратора"""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
        )


class ISAdminAuthorOrSuperuser(permissions.BasePermission):
    """
    Get - все пользователи
    Post - все авторизованные
    Все оставшиеся - только административный персонал и автор.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            or request.method in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj.author
            or request.user.is_admin
            or request.user.is_moderator
            if request.user.is_authenticated
            else request.method in permissions.SAFE_METHODS
        )
