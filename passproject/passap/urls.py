from django.urls import path
from passap import views

app_name='passap'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('userlogin/',views.user_login,name='user_login'),
]