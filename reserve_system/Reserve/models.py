from django.db import models
from django.contrib.auth.models import AbstractUser,User



class CustomUser(User):
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    

class Rserve(models.Model):
    need = models.TextField(default="None")
    date = models.DateField(default=None, null=True)
    reserve_id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reserves',null=True)
    gender = models.CharField(max_length=10, default='Male')
