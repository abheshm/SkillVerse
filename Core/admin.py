from django.contrib import admin
from .models import User
from .models import Customer
from .models import Technician
from .models import ServiceRequest
from .models import Bill
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(ServiceRequest)
admin.site.register(Bill)




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