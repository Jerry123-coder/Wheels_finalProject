from django.urls import path
from . import views
from django.contrib.auth import views as LogViews

urlpatterns = [    
    path('', views.home, name='home_page'),
    path('wheels/', views.wheels , name='wheels_page'), 
    path('addCon/', views.addCon, name='addCon_page'),
    
    path('wallet/', views.wallet, name='wallet_page'),
    path('createPin/', views.createPin,name='createPin_page'),
    
    path('driverLog/', views.driverLog, name='driverLog_page'),
    path('agentLog/', views.agentLog, name='agentLog_page'),
    path('timeLog/', views.timeLog, name='timeLog_page'),
    
    path('deposit/', views.deposit, name='deposit_page'),
    
    path('register/', views.register, name='register_page'),
    path('login/', LogViews.LoginView.as_view(template_name='Log/login.html'), name='login_page'),
    path('logout/', LogViews.LogoutView.as_view(template_name='Log/logout.html'), name='logout_page'),
]