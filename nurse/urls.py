from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('nurse-dashboard/', views.nurse_interface, name="nurse_interface")
]
