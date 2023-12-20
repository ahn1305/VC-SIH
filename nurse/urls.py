from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('nurse-dashboard/', views.nurse_interface, name="nurse_interface"),
   path('getPatientData', views.getData),
   path('compare-and-display/', views.compare_and_display, name='compare_and_display'),


]
