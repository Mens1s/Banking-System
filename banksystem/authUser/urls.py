from django.urls import path
from . import views
# from main import viewas as v
urlpatterns = [
    path("register", views.register, name = "register"),
    path("login", views.loginreq, name = "login"),
    path("", views.loginreq),
]