from django.urls import path
from . import views

urlpatterns = [
    path('', views.point_of_sale_home, name="point_of_sale_home"), 
]
