from django.urls import path, include
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.all_products, name="all-products"),
    path("product/<slug:slug>", views.single_product, name="single-product"),
    path("blogs", views.blogs, name="blogs"),
    path("cart", views.cart, name="cart"),
    path("add-to-cart/<product_id>", views.add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<product_id>", views.remove_from_cart, name="remove-from-cart"),
    path("checkout", views.checkout, name="checkout"),
    path('contact-us', views.contect, name="contact-us")
]
