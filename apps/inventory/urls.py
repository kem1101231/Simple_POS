from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.inventory_list, name="inventory_list"), 
]
