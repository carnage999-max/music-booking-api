from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import LoginUserview, LogoutView, RegisterUserViewSet


router = DefaultRouter()
router.register('register', RegisterUserViewSet, basename='register-user')
router.register('login', LoginUserview, basename='login-user')

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', LogoutView, name='logout')
]

