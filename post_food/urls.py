from django.urls import path
from . import views
# def update_orders(request, id):

urlpatterns = [
    path('doner', views.doner, name='doner'), 
    path('post', views.post, name='post'), 
    path('<int:id>/', views.view_food, name='view_food'), 
    path('ngo', views.ngo, name='ngo'),
    path('order', views.order, name='order'),
    path('dis_order', views.dis_order, name="dis_order"),
    path('Delete_food/<int:id>/', views.Delete_food, name='Delete_food'),
    path('update_orders/<int:id>/', views.update_orders, name='update_orders'),
]