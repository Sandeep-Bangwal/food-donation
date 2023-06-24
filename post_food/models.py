from django.db import models
import datetime
# Create your models here.

class food_list (models.Model):
    food_id = models.AutoField(primary_key=True)
    food_title = models.CharField(max_length=50)
    Rst_name = models.CharField(max_length=50)
    user_post_id = models.IntegerField()
    location = models.CharField(max_length=100)
    packets = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images")
    time = models.CharField(max_length=10)
    date = models.CharField(max_length=11)


class Order_list (models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    food_id = models.ForeignKey(food_list, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, default="waiting")
    date = models.DateField(default=datetime.datetime.today)
