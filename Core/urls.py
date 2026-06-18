from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet , TechnicianViewSet,ServiceRequestViewSet,BillViewSet


from .views import TestAuthView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('customer', CustomerViewSet)
router.register('technician', TechnicianViewSet)
router.register('service-requests', ServiceRequestViewSet)
router.register('bills', BillViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/test-auth/', TestAuthView.as_view()),
]



