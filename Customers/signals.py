from .models import Wallet
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(holder=instance)

@receiver(post_save, sender=User)
def save_wallet(sender, instance, **kwargs):
    instance.wallet.save()