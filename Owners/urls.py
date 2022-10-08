from django.urls import path
from . import views


urlpatterns = [    
    path('owner/', views.home , name='ownerHome_page'), 
    path('owallet/', views.wallet, name='owallet_page'),
    path('createCon/', views.CreateCon.as_view(), name='createCon_page'),
    path('conInfo/<int:pk>/', views.ConInfo.as_view(), name='conInfo_page'),
    path('updateCon/<int:pk>/', views.UpdateCon.as_view(), name='updateCon_page'),
    path('deleteCon/<int:pk>/', views.DeleteCon.as_view(), name='deleteCon_page'),
    
    path('owner/register/', views.ownerRegister, name='ownerRegister_page'),
    path('owner/login/', views.ownerLogin, name='ownerLogin_page'),
    #path('owner/logout/', views.ownerLogout, name='o_logout_page'),
]