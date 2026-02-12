from rest_framework import serializers
from .models import Booking, Service
from services.serializers import ServiceSerializer

class BookingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        source='service',
        write_only=True
    )

    customer_username = serializers.CharField(source='customer.username', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'service',
            'service_id',
            'customer_username',
            'booking_date',
            'status',
            'created_at',
        ]


