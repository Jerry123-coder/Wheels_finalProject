from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
import geocoder

class TruckDepot(models.Model):
    region = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.region
    
    def save(self, *args, **kwargs):
        location = self.location
        uLocation = geocoder.osm(location)
        self.long = uLocation.lng
        self.lat = uLocation.lat   
        return super(TruckDepot, self).save(*args, **kwargs)

class Truck(models.Model):
    name = models.CharField(max_length=100) 
    image = models.ImageField(default='default.jpg', upload_to='truck_pics')
    rate = models.FloatField(default=1)
    speed = models.FloatField(default=1)
    weight_level = models.IntegerField(default=1) 
    time_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name    

class Driver(models.Model):
    username = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    avatar = models.ImageField(default='default.jpg', upload_to='driver_pics')
    station = models.ForeignKey(TruckDepot,default=1, on_delete=models.CASCADE)
    active_since = models.DateTimeField(default= timezone.now)
    
    def __str__(self):
        return f"{self.username} {self.station.location} "