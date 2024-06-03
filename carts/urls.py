from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart-page"),
    path("product/add", views.add_product_to_basket, name="add-to-basket"),
    path("product/remove/<slug:product_slug>", views.remove_product_from_basket, name="remove-from-basket"),
    path("product/increase/<slug:product_slug>", views.increase_product_quantity, name="increase-quantity"),
    path("product/decrease/<slug:product_slug>", views.decrease_product_quantity, name="decrease-quantity"),
    
]
