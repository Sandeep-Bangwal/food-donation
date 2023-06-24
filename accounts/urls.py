from django.urls import path
from . import views

urlpatterns = [
    path('singup', views.singup, name='singup'),
    path('login',views.login, name = 'login'),
    path('logout',views.logout, name = 'logout'),
    path('admin',views.admin, name = 'admin'),
   
    path('approve_user/<int:id>',views.approve_user, name = 'approve_user'),
]