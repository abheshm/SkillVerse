from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import User,Bill,ServiceRequest, Technician,Customer,TechnicianApplication
from .serializers import UserSerializer,BillSerializer,ServiceRequestSerializer,TechnicianSerializer,CustomerSerializer,TechnicianApplicationSerializer
from .permissions import IsAdmin,IsTechnician,IsCustomer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):

        serializer = self.get_serializer(
            request.user
        )

        return Response(serializer.data)
    # permission_classes = [IsAdmin]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsCustomer]

class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer

    @action(
    detail=False,
    methods=['get']
    )
    def my_jobs(self, request):

        technician = Technician.objects.get(user=request.user)

        jobs = ServiceRequest.objects.filter(
        assigned_technician=technician
        )

        serializer = ServiceRequestSerializer(
        jobs,
        many=True
        )

        return Response(serializer.data)

    # permission_classes = [IsTechnician]

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def perform_create(self, serializer):

        customer = Customer.objects.get(
            user=self.request.user
        )

        serializer.save(
            customer=customer,
            status='pending'
        )

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAdmin]
    )
    def assign_technician(self, request, pk=None):

        service_request = self.get_object()

        technician_id = request.data.get(
            'technician_id'
        )

        try:

            technician = Technician.objects.get(
                pk=technician_id
            )

            service_request.assigned_technician = (
                technician
            )

            service_request.status = 'assigned'

            service_request.save()

            return Response(
                {'status': 'Technician assigned'}
            )

        except Technician.DoesNotExist:

            return Response(
                {'error': 'Technician not found'},
                status=status.HTTP_400_BAD_REQUEST
            )
        

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):

        service_request = self.get_object()

        service_request.status = 'completed'

        service_request.save()

        return Response({
            'status': 'Service request marked completed'
        })   
    

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    # permission_classes = [IsAdmin | IsTechnician | IsCustomer ]


from rest_framework.views import APIView

class TestAuthView(APIView):

    def get(self, request):

        return Response({
            "headers": dict(request.headers)
        })

class TechnicianApplicationViewSet(viewsets.ModelViewSet):

    queryset = (
        TechnicianApplication.objects.all()
    )

    serializer_class = (
        TechnicianApplicationSerializer
    )

    def get_permissions(self):

        if self.action in ["create", "my_application"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]

        return [permission() for permission in permission_classes]

    @action(
    detail=True,
    methods=['post']
    )
    def approve(self, request, pk=None):

        application = self.get_object()


        technician, created = Technician.objects.get_or_create(
            user=application.user,
            defaults={
                "skill": application.skill,
                "availability": application.availability
            }
        )


        application.status = "approved"

        application.save()


        return Response(
            {
                "status": "Technician approved"
            }
        )
    @action(
    detail=True,
    methods=['post']
    )
    def reject(self, request, pk=None):

        application = self.get_object()


        if application.status == 'rejected':

            return Response(
                {
                    "error": "Application already rejected"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


        application.status = "rejected"

        application.save()


        return Response(
            {
                "status": "Technician application rejected"
            }
        )

    @action(
    detail=False,
    methods=['get'],
    permission_classes=[IsAuthenticated]
    )
    def my_application(self, request):

        application = TechnicianApplication.objects.filter(
            user=request.user
        ).first()

        if not application:

            return Response(
                {
                    "status": "not_applied"
                }
            )

        serializer = self.get_serializer(
            application
        )

        return Response(serializer.data)

class AdminStatsView(APIView):

    permission_classes = [IsAdmin]


    def get(self, request):

        customer_count = Customer.objects.count()

        technician_count = Technician.objects.count()

        pending_applications = TechnicianApplication.objects.filter(
            status="pending"
        ).count()

        service_request_count = ServiceRequest.objects.count()


        return Response({

            "customers": customer_count,

            "technicians": technician_count,

            "pending_applications": pending_applications,

            "service_requests": service_request_count

        })