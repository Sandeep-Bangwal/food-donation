from django.shortcuts import render, HttpResponse
from post_food.models import food_list

# Create your views here.


def home(request):
  food_items = food_list.objects.all()
  return render(request, "home.html", {'food_items': food_items})


