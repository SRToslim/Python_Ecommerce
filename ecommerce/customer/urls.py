from django.urls import path

from .views import *

urlpatterns = [
    path('dashboard/', UserDashboard, name='userDashboard'),
    path('order-history/', CustomerOrder, name='userOrder'),
    path('profile/', CustomerInfo, name='userProfile'),
]
