from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/mobile/otp/', login_otp, name='otp'),
    path('login/', email_login, name='login'),
    path('login/mobile/', mobile_login, name='mobile'),
    path('logout/', logout_view, name='logout'),
]
