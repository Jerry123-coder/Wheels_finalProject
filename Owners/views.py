from django.shortcuts import render,redirect
from .models import Owner,LogCache,Wallet,Container
from Customers.models import TransactionLog
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from bitcoin import *
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView

def ownerRegister(request):
    if request.method == 'POST':
        owner = Owner()
        owner.username = request.POST['username']
        owner.email = request.POST['email']
        owner.password1 = request.POST['password1']
        owner.password2 = request.POST['password2']
        #referenced variables
        username = owner.username
        email = owner.email
        password1 = owner.password1
        password2 = owner.password2
        ############
        if username == "" or email == "":
            messages.info(request, 'all fields are required')
            return redirect('ownerRegister_page')
        elif owner.isExists():
            messages.info(request, 'username already taken')
            return redirect('ownerRegister_page')
        elif password1 != password2:
            messages.info(request, 'passwords dont match')
            return redirect('ownerRegister_page')
        elif len(password1) < 4:
            messages.info(request, 'password too short at least 4 xtcs')
            return redirect('ownerRegister_page')
        elif len(username) < 4 :
            messages.info(request, 'username too short at least 4 xtcs')
            return redirect('ownerRegister_page')
        else:
            owner.password1 = make_password(owner.password1)
            owner.save()
            return redirect('ownerLogin_page')
    return render(request, 'ownerLog/register.html')

def ownerLogin(request):
    if request.method == "POST":
        logs = LogCache()
        logs.username = request.POST['username']
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        owner =  Owner.get_Owner_by_username(username)
        if owner:
            flag = check_password(password1, owner.password1)
            if flag:
                logs.save()
                print(username)
                return redirect('ownerHome_page')
            else:
                messages.info(request, 'invalid usermane or password')
        else:
            messages.info(request, 'invalid usermane or password')
    return render(request, 'ownerLog/login.html')     

def home(request):
    logs = LogCache.objects.all().last()
    logCount = LogCache.objects.all().count()
    if logCount > 1:
        LogCache.objects.all().first().delete()
    cUser = Owner.objects.filter(username=logs).last()
    cuid = cUser.id
    ownerCon = Container.objects.filter(owner=cuid)
    print(ownerCon)
    print(cUser)
    context = {
        'logs' : LogCache.objects.all().last(),
        'containers' : Container.objects.filter(owner=cuid)
    }
    return render(request, 'ohome.html', context)

def wallet(request):
    logs = LogCache.objects.all().last()
    cUser = Owner.objects.filter(username=logs).last()
    bal = Wallet.objects.filter(holder=cUser).last().balance_BTC
    bal = "{:.3f}".format(bal)
    cuid = cUser.id
    if request.method == 'POST':
        oWallet = Wallet.objects.filter(holder=cUser).last()
        oWallet.private_key = random_key()
        oWallet.public_key = privtopub(oWallet.private_key)
        oWallet.address = pubtoaddr(oWallet.public_key)
        oWallet.save()       
    context = {
        'logs' : LogCache.objects.all().last(),
        'wallet' : Wallet.objects.filter(holder=cUser).last(),
        'transactions' : TransactionLog.objects.filter(container_owner=cUser),
        'balance' : f"{bal} BTC"
    }        
    return render(request, 'oWallet.html', context)


class ConInfo(DetailView):
    model = Container
    template_name = 'ad/conInfo.html'

class CreateCon(CreateView):
    model = Container
    fields = ['name', 'image', 'description', 'price_BTC', 'weight']
    template_name = 'ad/createCon.html'
    success_url = '/owner'
    
    logs = LogCache.objects.all().last()
    cUser = Owner.objects.filter(username=logs).last()
    def form_valid(self, form):
        form.instance.owner = self.cUser
        return super().form_valid(form)  
    
class UpdateCon(UpdateView):
    model = Container
    fields = ['name', 'image', 'description', 'price_BTC']
    template_name = 'ad/updateCon.html'
    
    logs = LogCache.objects.all().last()
    cUser = Owner.objects.filter(username=logs).last()
    def form_valid(self, form):
        form.instance.owner = self.cUser
        return super().form_valid(form)

class DeleteCon(DeleteView):
    model = Container
    template_name = 'ad/deleteCon.html'
    success_url = '/owner'      