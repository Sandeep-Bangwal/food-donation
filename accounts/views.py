from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from . models import users
from post_food.models  import food_list
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.hashers import  make_password, check_password # this make_password use for password hash and 
#chek_password use encode the password with two paramiter 1. password and objects.password where the ex users.password 


# Create your views here.
def singup(request):
   
   if request.method == 'GET':
      return render(request, 'singup.html')
   else: 
    request.method == "POST"
    # username = postData.get('Names') 
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    account = request.POST['account']
    name = request.POST['name']
    Address = request.POST['Address']
    
    ad = users(email = email, name=name, password = password, account = account, Address = Address ) 
    
    error_message = None
   
    #cheking froms validation 
    if len(password) < 3:
            error_message = 'Password Must be 3-6 characters long.'
    elif password != cpassword:
         error_message = 'Password does not match try again'
    #if user email addreess already Registered
    elif ad.isExit():
         error_message = 'Email Address Already Registered..'

    #nt any error masssges user data save into db
    if not error_message:
      #createing the password hash
      ad.password = make_password(ad.password)
      #save the recode into database
      ad.register()
      return  HttpResponse('singup scess')
    #if any error massages return again singup page and display error massges 
    else:
      return render(request, 'singup.html', {'error': error_message})
      
    
#function for login   
def login(request):
   if request.method == "POST":
      email = request.POST['email']
      password = request.POST['password']

      # below the us --> user objcts  and chek the email exit into db this get_user_by_email is method is defind in models.py
      us = users.get_users_by_email(email)

      if us: 
        #chek the password vaild 
        flag = check_password(password, us.password)
        if flag:
          request.session['user'] = us.sno
          request.session['user_Is_doner'] = us.account 
          print(request.session['user_Is_doner'] )
          roles = users.objects.filter(email = us.email , account ='NGO', status = 1)                                                              
          if roles: 
           return redirect("/post_food/ngo")
          elif users.objects.filter(email = us.email , account ='Doner', status = 1) :
            return redirect("/post_food/doner",{'roles': roles})
          elif users.objects.filter(email = us.email , account ='Admin') :
            return redirect('admin')
          else:
            return HttpResponse("Your Account Not verify......Plz try Again Later.......")
               
        else:
         return HttpResponse("invaild password or email plx try agin")
      else:
         return HttpResponse("email addres not fond")
      
    
   return render(request, "login.html")

#log out views 
def logout(request):
   request.session.clear()
   return redirect('login')

def admin(request):
   lists = users.objects.filter(status=0)
   return render(request, 'admin.html', {'lists': lists})

def approve_user(request, id):
  approve = users.objects.filter(sno = id).update(status=1)
  return HttpResponseRedirect(reverse('admin'))

