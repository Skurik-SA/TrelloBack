import uuid

from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile (models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    quotation = models.TextField(max_length=255, blank=True)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
