from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import BookingRequestViewSet, EventViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


router = DefaultRouter()
router.register('bookings', BookingRequestViewSet, basename='booking-requests')
router.register('events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls))
]

schema_view = get_schema_view(
    openapi.Info(
        title="Music Booking API",
        default_version="v1",
        description="API for booking music events and artists",
        contact=openapi.Contact(name="API Support", email="jamesezekiel039@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns += [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

