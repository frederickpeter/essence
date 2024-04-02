from django.urls import path, include
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.all_products, name="all-products"),
    path("catgeory/<gender>/<slug:slug>", views.category_products, name="category-products"),
    path('type/<slug:name>', views.type_products, name='type-products'),
    path("blogs", views.blogs, name="blogs"),
]
