from django.urls import path
from .views import (
    nurse_interface
)

urlpatterns = [
   path('nurse-dashboard/', nurse_interface, name="nurse_interface")
]
