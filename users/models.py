from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


USERTYPES = (
        ('artist', 'Artist'),
        ('organizer', 'Organizer'),
        ('admin', 'Admin'),
    )

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', USERTYPES[2][0])

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True "
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True"
            )

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):    
    username = models.CharField(max_length=200, blank=True, null=True)
    user_type = models.CharField(_("User type"), max_length=10, choices=USERTYPES)
    # COMMON FIELDS FOR ALL USER TYPES
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    phone_number = models.CharField(max_length=13, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    
    
class ArtistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='artist_profile', verbose_name=_("Artist"))
    stage_name = models.CharField(_("Stage name"), max_length=255)
    genre = models.CharField(max_length=50, verbose_name=_("Genre"))
    availability = models.BooleanField(default=True, verbose_name=_("Availability"))
    website = models.URLField(blank=True, null=True, verbose_name=_("Website URL"))
    social_links = models.JSONField(blank=True, null=True, verbose_name=_("Social Links"))
    bio = models.TextField(blank=True, null=True, verbose_name=_("Bio")) 
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class OrganizerProfile(models.Model):
    user = models.OneToOneField("CustomUser", verbose_name=_("Organizer"), on_delete=models.CASCADE, related_name="organizer_profile")
    company_name = models.CharField(_("Company name"), max_length=255)
    description = models.TextField(_("Description"))
    website = models.URLField(blank=True, null=True, verbose_name=_("Website URL"))
    social_links = models.JSONField(blank=True, null=True, verbose_name=_("Social Links"))
    bio = models.TextField(blank=True, null=True, verbose_name=_("Bio")) 
    
    def __str__(self):
        return self.user
