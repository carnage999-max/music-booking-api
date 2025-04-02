from rest_framework.permissions import BasePermission


class IsLoggedIn(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated
    
class IsArtist(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'artist'
    
class IsOrganizer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'organizer'
