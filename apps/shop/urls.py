from django.urls import path, include
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('catgeory/<slug:slug>', views.categories, name='category'),
    path('blogs', views.blogs, name='blogs')
]