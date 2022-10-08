from django.contrib import admin
from .models import Owner,LogCache,Wallet,Container

admin.site.register(Owner)
admin.site.register(LogCache)
admin.site.register(Wallet)
admin.site.register(Container)
