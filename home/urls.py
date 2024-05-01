from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("category/<slug:category_slug>/", views.show_product_by_category, name="category-page"),
]
