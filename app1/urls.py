from app1.views import *
from django.urls import path

app_name='soulmate'
urlpatterns=[
    path('pichhuk/',pichhuk,name='pichhuk')
]