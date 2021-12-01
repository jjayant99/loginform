from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('', views.logoutUser, name="logout"),
]