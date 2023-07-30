from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vege(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    receipe_name=models.CharField(max_length=100)
    receipe_dis=models.TextField()
    receipe_img=models.ImageField(upload_to="recipe")
     
