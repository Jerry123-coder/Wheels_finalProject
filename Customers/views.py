import math
from django.shortcuts import render,redirect
from .forms import RegisterForm
from Caches.models import ContCache
from Drivers.models import Truck
from Owners.models import Container
from django.contrib import messages
from .models import Wallet,TransactionLog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from bitcoin import *
from django.http import JsonResponse
import json
from forex_python.bitcoin import BtcConverter

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            form.save()
            return redirect('wallet_page')
    else:
        form = RegisterForm()
    return render(request, 'Log/register.html', {'form':form})

def home(request):
    return render(request, 'home.html')

@login_required
def wheels(request):
    bit = BtcConverter()
    bitx = bit.get_latest_price('GHS')
    ConkeyCount = ContCache.objects.all().count()
    if ConkeyCount > 0:
        Conkey = ContCache.objects.all().last().key
        weight = ContCache.objects.all().last().weight_In
        weight = math.trunc(weight)
        tlevel = ContCache.objects.all().last().truck
        container = Container.objects.filter(weight=Conkey).last()
        truck = Truck.objects.filter(weight_level=tlevel).last()
        price = Container.objects.filter(weight=Conkey).last().price_BTC
        price = "{:.3f}".format(price * bitx)
    else:
        weight = ''
        container = ''
        price = ''
        truck = ''

    context = {
        'container' : container, 
        'weight' : f"{weight} kg",
        'price_ghs' : f"{price} GHS",
        'truck' : truck
    }
    return render(request, 'wheels.html', context)

def addCon(request):
    data = json.loads(request.body)
    container = data['container']
    weight = data['weight']
    truck = data['truck']
    if container == 0:
        messages.info(request, 'Weight at least 1 at most 10000kg')
        ContCache.objects.all().delete()
    else:
        contCache = ContCache()
        contCache.key = container
        contCache.weight_In = weight
        contCache.truck = truck
        contCache.save() 
        contCacheCount = ContCache.objects.all().count()
        if contCacheCount > 3:
            ContCache.objects.all().first().delete()
    return JsonResponse('addCon', safe=False)

@login_required
def wallet(request):
    bal = Wallet.objects.filter(holder=request.user).last().balance_BTC
    bal = "{:.3f}".format(bal)
    wallet = Wallet.objects.filter(holder=request.user).last()
    if request.method == 'POST':
        wallet.private_key = random_key()
        wallet.public_key = privtopub(wallet.private_key)
        wallet.address = pubtoaddr(wallet.public_key)
        wallet.save()       
    context = {
        'balance' : f"{bal} BTC",
        'wallet' : Wallet.objects.filter(holder=request.user).last(),
        'transactions': TransactionLog.objects.filter(name=request.user)
    }        
    return render(request, 'wallet.html', context)

def createPin(request):
    data = json.loads(request.body)
    pin = data['pin']
    wallet = Wallet.objects.filter(holder=request.user).last()
    wallet.pin_code = pin
    wallet.pin_code = make_password(wallet.pin_code)
    wallet.save()
    return JsonResponse('createPin', safe=False)

@login_required
def deposit(request):
    wallet = Wallet.objects.filter(holder=request.user).last()
    if request.method == "POST":
        pin1 = request.POST.get('pin1')
        pin2 = request.POST.get('pin2')
        pin3 = request.POST.get('pin3')
        pin4 = request.POST.get('pin4')
        amount = request.POST.get('amount')
        pinCode = pin1 + pin2 + pin3 + pin4
        match = check_password(pinCode, wallet.pin_code)
        if match:
            wallet.balance_BTC = float(amount) + wallet.balance_BTC
            wallet.save()
        else:
            messages.info(request, f"invalid user pin")
    bal = wallet.balance_BTC
    bal = "{:.3f}".format(bal)
    bit = BtcConverter()
    bitx = bit.get_latest_price('GHS')
    context = {
        'balance' : f"{bal} BTC",
        'bal' : bal,
        'wallet' : wallet,
        'bitx' : bitx
    }
    return render(request, 'deposit.html', context)

@login_required
def driverLog(request):
    bal = Wallet.objects.filter(holder=request.user).last().balance_BTC
    bal = "{:.3f}".format(bal)
    context = {
        'balance' : f"{bal} BTC",
        'wallet' : Wallet.objects.filter(holder=request.user).last(),
        'transactions': TransactionLog.objects.filter(name=request.user)
    }        
    return render(request, 'TransLog/driverLog.html', context)

@login_required
def agentLog(request):
    bal = Wallet.objects.filter(holder=request.user).last().balance_BTC
    bal = "{:.3f}".format(bal) 
    context = {
        'balance' : f"{bal}",
        'wallet' : Wallet.objects.filter(holder=request.user).last(),
        'transactions': TransactionLog.objects.filter(name=request.user)
    }        
    return render(request, 'TransLog/agentLog.html', context)

@login_required
def timeLog(request):
    bal = Wallet.objects.filter(holder=request.user).last().balance_BTC
    bal = "{:.3f}".format(bal)       
    context = {
        'balance' : f"{bal}",
        'wallet' : Wallet.objects.filter(holder=request.user).last(),
        'transactions': TransactionLog.objects.filter(name=request.user)
    }        
    return render(request, 'TransLog/timeLog.html', context)