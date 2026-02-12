from django.db import models
from django.conf import settings

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


User = settings.AUTH_USER_MODEL

class ProviderProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='provider_profile'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='providers'
    )
    location = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.service.name}"