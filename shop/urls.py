from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<slug:slug>/", views.product_details, name="product_details"),
    path("cart", views.cart, name="cart"),
    path("add_to_cart/<slug:slug>/", views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("signup/", views.signup, name="signup"),
    path("ai_recipe/", views.ai_recipe, name="ai_recipe"),
]