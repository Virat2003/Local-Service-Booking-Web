from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('provider', 'Provider'),
        ('admin', 'Admin'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='customer'
    )
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    # address = models.TextField(blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)
    # state = models.CharField(max_length=100, blank=True, null=True)
    # pincode = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


