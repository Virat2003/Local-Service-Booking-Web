from django.urls import path
from .views import (
    CreateBookingView,
    CustomerBookingsView,
    ProviderBookingsView,
    UpdateBookingStatusView
)

urlpatterns = [
    path('create/', CreateBookingView.as_view()),
    path('my/', CustomerBookingsView.as_view()),
    path('provider/', ProviderBookingsView.as_view()),
    path('update/<int:booking_id>/', UpdateBookingStatusView.as_view()),
]
