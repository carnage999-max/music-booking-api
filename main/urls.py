from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import BookingRequestViewSet, EventViewSet


router = DefaultRouter()
router.register('bookings', BookingRequestViewSet, basename='booking-requests')
router.register('events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls))
]

