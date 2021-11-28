from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path("register/", views.user_registration, name = "register"),
    path("login/", views.user_login, name="login"),
    path("contact/", views.contact, name="contact"),
    # after user login
    path("home/", views.user_home, name="home"),
    path("logout/", views.user_logout, name="logout"),
    
]
