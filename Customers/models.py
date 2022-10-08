from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Wallet(models.Model):
    private_key = models.CharField(default='***',max_length=300)
    public_key = models.CharField(default='***',max_length=300)
    address = models.CharField(default='***',null=True,max_length=300)
    pin_code = models.CharField(default='null', max_length=4)
    balance_BTC = models.FloatField(default=10)
    time_created = models.DateTimeField(default=timezone.now)    
    holder = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.holder.username

class TransactionLog(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    pickup = models.CharField(max_length=200)
    dropoff = models.CharField(default="Accra", max_length=200)
    container = models.CharField(default='1',  max_length=200)
    container_owner = models.CharField(default='1', max_length=200)
    agent_location = models.CharField(default='1', max_length=200)
    agent = models.CharField(default=1, max_length=300)
    agent_phone = models.CharField(default=1, max_length=50)
    depot_location = models.CharField(default='1', max_length=200)
    driver = models.CharField(default=1, max_length=300)
    driver_phone = models.CharField(default=1, max_length=50)
    trip_distance = models.CharField(default='1', max_length=200)
    delivery_type = models.CharField(default='1', max_length=100)
    delivery_fee_BTC = models.FloatField(default=1)
    delivery_duration = models.CharField(default=1, max_length=100)
    duration_stamp = models.IntegerField(default=1)
    amount_GHS = models.FloatField(default=1)
    amount_BTC = models.FloatField(default=1)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name.username