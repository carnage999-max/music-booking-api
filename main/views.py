from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import BookingRequest, Event
from .serializers import BookingRequestSerializer, EventSerializer


class BookingRequestViewSet(viewsets.ModelViewSet):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
    
    def create(self, request, *args, **kwargs):
        """Create a booking request for an artist."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Validate double-booking
            artist = serializer.validated_data.get('artist')
            event_date = serializer.validated_data.get('event_date')
            if BookingRequest.objects.filter(artist=artist, event_date=event_date, status="accepted").exists():
                return Response({"error": "Artist is already booked for this date."}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['patch'])
    def respond(self, request, pk=None):
        """Allow artists to accept or decline a booking request."""
        booking = get_object_or_404(BookingRequest, pk=pk)
        status_choice = request.data.get("status")
        
        if status_choice not in ["accepted", "declined"]:
            return Response({"error": "Invalid status choice."}, status=status.HTTP_400_BAD_REQUEST)
        
        booking.status = status_choice
        booking.save()
        
        # If accepted, create the event or add the artist to an existing event
        if status_choice == "accepted":
            event, created = Event.objects.get_or_create(name=booking.event_name, date=booking.event_date)
            event.artists.add(booking.artist)
        
        return Response({"message": f"Booking {status_choice}."}, status=status.HTTP_200_OK)

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

