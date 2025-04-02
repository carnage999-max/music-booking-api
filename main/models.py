from django.db import models


class BookingRequest(models.Model):
    artist = models.ForeignKey('users.ArtistProfile', on_delete=models.CASCADE, related_name='booking_requests')
    event_name = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    status = models.CharField(
         max_length=10,
         choices=[("pending", "Pending"), ("accepted", "Accepted"), ("declined", "Declined")
        ], default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.artist
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    artists = models.ManyToManyField('users.ArtistProfile', related_name='events')
    
