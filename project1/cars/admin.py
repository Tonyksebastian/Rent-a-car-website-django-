from django.contrib import admin
from .models import car
from .models import Booking
# Register your models here.
admin.site.register(car)
admin.site.register(Booking)