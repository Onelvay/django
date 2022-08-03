from django.urls import path
from django.urls import re_path
from functions import views

urlpatterns = [
    path('', views.home),
    re_path(r'^add', views.Create_Post),
    re_path(r'^register',views.registration)
]
