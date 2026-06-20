from django.contrib import admin
from .models import User
from .models import Customer
from .models import Technician
from .models import ServiceRequest
from .models import Bill
from .models import TechnicianApplication

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(ServiceRequest)
admin.site.register(Bill)
admin.site.register(TechnicianApplication)




# abm
# abm@gmail.com
# abm@123


# Username : john123
# Email    : john@gmail.com
# Password : 123456
# Role     : customer


# Username : mathew123
# user id  : 15
# tech id  : 3
# Email    : mathew@gamil.com
# Password : 123456
# Role     : technician
# {"id":15,"last_login":null,"is_superuser":false,
#  "username":"mathew123","first_name":"mathew","last_name":"",
#  "email":"mathew@gmail.com","is_staff":false,"is_active":true,
#  "date_joined":"2026-06-15T18:37:38.918089Z","role":"technician","groups":[],"user_permissions":[]}


# {
#     "username": "techapplicant",
#     "email": "techapplicant@gmail.com",
#     "password": "test12345",
#     "role": "technician"
# }
# {"id":16,"last_login":null,"is_superuser":false,"username":"techapplicant","first_name":"","last_name":"",
#  "email":"techapplicant@gmail.com","is_staff":false,"is_active":true,"date_joined":"2026-06-19T06:29:18.792124Z",
#  "role":"technician","groups":[],"user_permissions":[]}
# {
#         "id": 16,
#         "last_login": null,
#         "is_superuser": false,
#         "username": "techapplicant",
#         "first_name": "",
#         "last_name": "",
#         "email": "techapplicant@gmail.com",
#         "is_staff": false,
#         "is_active": true,
#         "date_joined": "2026-06-19T06:29:18.792124Z",
#         "role": "technician",
#         "groups": [],
#         "user_permissions": []
#     }
# {"id":1,"full_name":"Tech Applicant","skill":"Laptop Repair",
#  "experience":"2 Years","availability":true,"status":"pending",
#  "created_at":"2026-06-19T06:50:25.701363Z","user":16}