from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from services.models import ProviderProfile   # adjust import if needed


@receiver(post_save, sender=User)
def create_provider_profile(sender, instance, created, **kwargs):
    if created and instance.role == "provider":
        ProviderProfile.objects.create(user=instance)
