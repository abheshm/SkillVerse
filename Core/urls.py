from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet , TechnicianViewSet,ServiceRequestViewSet,BillViewSet,TechnicianApplicationViewSet


from .views import TestAuthView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('customer', CustomerViewSet)
router.register('technician', TechnicianViewSet)
router.register('service-requests', ServiceRequestViewSet)
router.register('bills', BillViewSet)
router.register('technician-applications',TechnicianApplicationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/test-auth/', TestAuthView.as_view()),
]



