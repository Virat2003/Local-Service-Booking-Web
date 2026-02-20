from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Booking
from .serializers import BookingSerializer
from services.models import ProviderProfile


class CreateBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        if request.user.role != 'customer':
            return Response(
                {"error": "Only customers can book services"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = BookingSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Get service from validated data
        service = serializer.validated_data['service']

        # ✅ Auto assign provider from service
        booking = serializer.save(
            customer=request.user,
            provider=service.provider,
            status='pending'
        )

        return Response(
            BookingSerializer(booking).data,
            status=status.HTTP_201_CREATED
        )




class CustomerBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(customer=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
    

class ProviderBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'provider':
            return Response(
                {"error": "Only providers can view this"},
                status=status.HTTP_403_FORBIDDEN
            )

        bookings = Booking.objects.filter(provider=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)



class UpdateBookingStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=404)

        if request.user != booking.provider:
            return Response(
                {"error": "You are not allowed to update this booking"},
                status=status.HTTP_403_FORBIDDEN
            )

        new_status = request.data.get("status")

        if new_status not in ['accepted', 'rejected', 'completed']:
            return Response(
                {"error": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.status = new_status
        booking.save()

        return Response(
            {"message": f"Booking {new_status} successfully"}
        )

class CancelBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, booking_id):

        try:
            booking = Booking.objects.get(id=booking_id, customer=request.user)
        except Booking.DoesNotExist:
            return Response({
                "error":"Booking Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        if booking.status.lower() != "pending":
            return Response({
                "error":"Only Pending bookings can be cancelled"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        booking.status = "cancelled"
        booking.save()

        return Response({
            "message":"Booking cancelled Successfully"
        }, status=status.HTTP_200_OK)
