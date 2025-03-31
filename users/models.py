from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    USERTYPES = (
        ('artist', 'Artist'),
        ('client', 'Client'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(
        max_length=10,
        choices=USERTYPES,
        default='client',
        verbose_name=_("User Type"),
    )
    bio = models.TextField(blank=True, null=True, verbose_name=_("Bio"))
    
    
class ArtistProfile(models.Model):
    user = models.OneToOneField(CustomUser, ondeto_delete=models.CASCADE, related_name='artist_profile', verbose_name=_("User"))
    genre = models.CharField(max_length=50, verbose_name=_("Genre"))
    availability = models.BooleanField(default=True, verbose_name=_("Availability"))
    website = models.URLField(blank=True, null=True, verbose_name=_("Website URL"))
    social_links = models.JSONField(blank=True, null=True, verbose_name=_("Social Links"))
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    
class Event(models.Model):
    pass

