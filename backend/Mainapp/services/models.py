from django.db import models
from django.conf import settings
from account.models import User

class Service(models.Model):
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="services",
        limit_choices_to={'role': 'provider'}
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.provider.username}"



User = settings.AUTH_USER_MODEL


class ProviderProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='provider_profile',
        limit_choices_to={'role': 'provider'}
    )

    location = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} (provider)"
