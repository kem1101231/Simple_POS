from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.shipments, name="shipments"),
    path('create/', views.add_shipment, name="add_shipment"),
]
