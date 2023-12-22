from django.urls import path
from Reserve.views import register,login,login_register,Tool,set_date

urlpatterns = [
    path('',login_register,name='index'),
    path('tool/',Tool,name='tool'),
    path('date/',set_date,name='date')
]
