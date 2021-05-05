from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.product_list, name="product_list"),
    path('create/', views.add_product, name="add_product"),
]
