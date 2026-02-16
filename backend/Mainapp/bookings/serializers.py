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

    customer_email = serializers.CharField(
        source='customer.email',
        read_only=True
    )
    
    customer_phone = serializers.CharField(
    source='customer.phone',
    read_only=True
    )
    
    # customer_address = serializers.CharField(source='customer.address', read_only=True)
    # customer_city = serializers.CharField(source='customer.city', read_only=True)
    # customer_state = serializers.CharField(source='customer.state', read_only=True)
    # customer_pincode = serializers.CharField(source='customer.pincode', read_only=True)




    class Meta:
        model = Booking
        fields = [
            'id',
            'service',
            'service_id',
            'customer_username',
            'customer_email',
            'customer_phone',
            'booking_date',
            'status',
            'address',
            'city',
            'state',
            'pincode',
            'created_at',
            # 'customer_address',
            # 'customer_city',
            # 'customer_state',
            # 'customer_pincode',
        ]


