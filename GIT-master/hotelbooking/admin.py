from django.contrib import admin
from .models import Room
from .models import Check_Availability
from .models import UserRegister
from .models import Contact

# Register your models here.
admin.site.register(Room)
admin.site.register(Check_Availability)
admin.site.register(UserRegister)
admin.site.register(Contact)

