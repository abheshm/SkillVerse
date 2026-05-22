from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import User,Bill,ServiceRequest, Technician,Customer
from .serializers import UserSerializer,BillSerializer,ServiceRequestSerializer,TechnicianSerializer,CustomerSerializer
from .permissions import IsAdmin,IsTechnician,IsCustomer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdmin]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsCustomer]

class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    permission_classes = [IsTechnician]

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    @action(detail=True , methods=['Post'], permission_classes=[IsAdmin])
    def assign_technician(self, request, pk=None):
        service_request = self.get_object()
        technician_id = request.data.get('technician_id')
        try:
            technician = Technician.objects.get(pk=technician_id)
            service_request.assigned_technician = technician
            service_request.status = 'assigned'
            service_request.save()
            return Response({'status':'Technician assigned'})
        except Technician.DoesNotExist:
            return Response ({'error': 'Technician not found'}, status=status.HTTP_400_BAD_REQUEST)
        
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAdmin | IsTechnician | IsCustomer ]





