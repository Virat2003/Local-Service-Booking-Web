from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework import status


class ServiceListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.filter(is_active=True)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class CreateServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != "provider":
            return Response(
                {"error": "Only providers can add services"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ServiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(provider=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


class MyServicesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        # Only provider allowed
        if request.user.role != "provider":
            return Response(
                {"error": "Only providers can view their services"},
                status=status.HTTP_403_FORBIDDEN
            )

        services = Service.objects.filter(provider=request.user)
        serializer = ServiceSerializer(services, many=True)

        return Response(serializer.data)
    
    
class MyServicesDetailView(APIView):
    def get_object(self, request,pk):
        try:
            return Service.objects.get(pk=pk, provider=request.user)
        except Service.DoesNotExist:
            return None
        
    def delete(self, request,pk):
        if request.user.role != "provider":
            return Response(
                {"error":"Only providers Allowed"}, status=status.HTTP_403_FORBIDDEN
            )
        else:
            service = self.get_object(request, pk)
            if not service:
                return Response({
                    "error":"Service not found"
                }, status=status.HTTP_404_NOT_FOUND)
            service.delete()
            return Response({
                "message":"Service deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
            
    def put(self, request, pk):
        
        if request.user.role != "provider":
            return Response({
                "error":"Only Providers Allowed"
            }, status=status.HTTP_403_FORBIDDEN)
            
            
        service = self.get_object(request,pk)
        if not service:
            return Response({
                "message":"Service not found"
            })
        serializer = ServiceSerializer(service, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        