from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import ArtistsViewSet, LoginUserview, LogoutView, RegisterUserViewSet, OrganizerViewSet


router = DefaultRouter()
router.register('register', RegisterUserViewSet, basename='register-user')
router.register('login', LoginUserview, basename='login-user')
router.register('artists', ArtistsViewSet, basename='artists')
router.register('organizers', OrganizerViewSet, basename='organizers')

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', LogoutView, name='logout')
]

