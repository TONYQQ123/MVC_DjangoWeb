from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
class Rserve(models.Model):
    # Gender=(
    #     ('M','Male'),
    #     ('F','Female'),
    #     ('O','Other')
    # )
    # name=models.CharField(max_length=200)
    # gender=models.CharField(max_length=1,choices=Gender)
    # need=models.TextField()
    date=models.DateField(default='2023-1-1',null=True)

class CustomUser(User):
    pass