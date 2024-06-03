from . import views
from django.urls import path

urlpatterns = [
    path("store/", views.store, name="store-page"),
    path("product/<slug:product_slug>/", views.show_product_detail_by_name, name="product-detail-page"),
    

]
