from rest_framework.permissions import BasePermission


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user and request.user.is_authenticated
        return True


class IsCommentAuthorOrPostAuthorOrAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.user and request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.method in ['PUT', 'PATCH', 'DELETE']:

            return (obj.author == request.user or obj.post.author == request.user or request.user.is_staff)

        return True
