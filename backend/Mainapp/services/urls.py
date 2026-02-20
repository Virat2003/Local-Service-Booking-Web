from django.urls import path
from .views import ServiceListView,ServiceDetailView,CreateServiceView, MyServicesView, MyServicesDetailView

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('create/', CreateServiceView.as_view(), name='create-service'),
    path('myservices/', MyServicesView.as_view(), name='my-services'),
    path('myservices/<int:pk>/', MyServicesDetailView.as_view(), name='my-services-detail'),

]
