from django.contrib import admin
from .models import Driver,Truck,TruckDepot

# Register your models here.
admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(TruckDepot)