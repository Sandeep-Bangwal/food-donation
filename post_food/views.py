from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from . models import food_list, Order_list
from accounts.models import users
from django.urls import reverse
from django.db.models import Subquery, OuterRef

# doner..
def doner(request): 
  food_items = food_list.objects.filter(user_post_id = request.session['user'])
  return render (request, "doner.html", {'food_items': food_items})

def post(request):
    if request.method == 'GET':
      return render(request, 'post_food.html')
    else:  
     request.method == "POST"
     Restaurant_Name = request.POST['Restaurant_Name']
     title = request.POST['title']
     id = request.POST['id']
     rst_Loaction = request.POST['rst_Loaction']
     Packets = request.POST['Packets']
     img = request.FILES['img']
     date = request.POST['date']
     Cock_time = request.POST['Cock_time']
    
     add_food = food_list(Rst_name = Restaurant_Name, food_title = title, user_post_id = id, location =  rst_Loaction, 
      packets = Packets,  image= img, time = Cock_time, date = date ) 
    
     error_message = None
   
    #cheking froms validation 
     if len(Packets) <= 1:
      error_message = 'Password must be 3 char long'

    #nt any error masssges user data save into db
    if not error_message:
      #save the recode into database
      add_food.save()
      return  HttpResponse('scess')
    #if any error massages return again singup page and display error massges
    
    else:
     return render(request, "post_food.html", {'error': error_message})

def view_food (request, id):
  view_foods= food_list.objects.filter(food_id = id)
  # this user for if user is NGO show buttion buy and DONER show the update & delete butttons 
  chek_user = users.objects.filter(sno = request.session['user'], account ='Doner')
  dir = {
       'view_foods': view_foods,
       'chek_user': chek_user
    }
  return render (request, "foodPost_view.html",dir)


# NGO
def ngo(request):
  food_items = food_list.objects.all()
  return render(request, "ngo.html", {'food_items': food_items})

#Orders by NGO to doners

def order(request):
  food_ids = request.POST['food_id']
  order_list = Order_list(user_id = request.session['user'], food_id=food_list(food_id = food_ids))
  order_list.save()
  return redirect('dis_order') 

def dis_order(request):

    # display the order made by ngo in ngo order list
    orders = Order_list.objects.filter(user_id = request.session['user'])
    if not orders:
        message = "You have not placed any."
        context = {'message': message}
    else:
        context = {
          'orders': orders, 
          }

    if request.session['user_Is_doner'] == 'Doner':
     users_subquery = users.objects.filter(sno=OuterRef('user_id')).values('name')
     food_list_subquery=food_list.objects.filter(user_post_id=request.session['user']).values('food_id')
     order= Order_list.objects.prefetch_related('food_id', 'user_id').annotate(user_name=Subquery(users_subquery)).filter(status='waiting', food_id__in=Subquery(food_list_subquery)).values('order_id', 'food_id__food_title','food_id__image', 'food_id__packets', 'date','user_name')

     if not order:
        message = "You have not placed any orders."
        context = {'message': message}
     else:
        context = {
          'order': order,
          }
    return render(request, "order.html", context)

# update the food posts
def update_orders(request, id):
  if request.method == "POST":
   status = request.POST['status']
   Update = Order_list.objects.get(order_id = id)
   Update.status =  status
   Update.save()
  return redirect("dis_order")

# delete the food post
def Delete_food(request, id):
    delete = food_list.objects.get(food_id = id)
    delete.delete()
    return HttpResponseRedirect(reverse('doner'))
