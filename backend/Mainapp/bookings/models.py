from django.db import models
from django.conf import settings
from services.models import Service

User = settings.AUTH_USER_MODEL

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='customer_bookings'
    )
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='provider_bookings'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )
    booking_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer} → {self.provider}"
