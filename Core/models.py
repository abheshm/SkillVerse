from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username
    

class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    

    def __str__(self):
        return self.user.username
    
class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('assigned','Assigned'),
        ('completed','Completed')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE , related_name= 'requests')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_technician = models.ForeignKey(Technician, on_delete= models.SET_NULL , null=True ,blank=True, related_name= 'assigned_jobs' )
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.description


class Bill(models.Model):
    PAYMENT_STATUS= (
        ('pending', 'Pending'),
        ('paid','Paid')
    )
    request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, null= True , blank= True)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentstatus = models.CharField(max_length=20, choices=PAYMENT_STATUS, default= 'pending')

    def save(self, *args, **kwargs):
        self.total_amount = self.service_charge + self.extra_charges
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Bill for request {self.request.id}"
    
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('technician','Technician')
    )
    role= models.CharField(max_length=20, choices=ROLE_CHOICES)



##test dose 