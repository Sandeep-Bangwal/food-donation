from django.db import models

# Create your models here.

class users(models.Model):
  sno = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  email= models.EmailField(max_length=254)
  password = models.CharField(max_length=500)
  account = models.CharField(max_length=10)
  Address = models.CharField(max_length=100)
  status= models.IntegerField(default=0)

  def register(self):
    self.save()

  #method for chek user email into db --> login time
  def get_users_by_email(email):
    try:
      return users.objects.get(email=email)
    except:
      return False

  #method for checking user singup time --> email exit or not 
 
  def isExit(self):
    if users.objects.filter(email=self.email):
      return True
    return  False
      