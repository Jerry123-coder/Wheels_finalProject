from django.db import models
from django.utils import timezone
from django.urls import reverse

class Owner(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    @staticmethod
    def get_Owner_by_username(username):
        try:
            return Owner.objects.get(username = username)
        except:
            return False
    
    def isExists(self):
        if Owner.objects.filter(username = self.username):
            return True
        return False

class LogCache(models.Model):
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Wallet(models.Model):
    private_key = models.CharField(default='***',max_length=300)
    public_key = models.CharField(default='***',max_length=300)
    address = models.CharField(default='***',max_length=300)
    balance_BTC = models.FloatField(default=0)
    time_created = models.DateTimeField(default=timezone.now)    
    holder = models.OneToOneField(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.holder.username     

class Container(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    description = models.TextField(max_length=100)
    price_BTC = models.FloatField()
    weight = models.FloatField(default=200)
    weight_range = models.CharField(default='kg', max_length=300)
    time_created = models.DateTimeField(default = timezone.now)     
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("conInfo_page", kwargs={"pk": self.pk})   