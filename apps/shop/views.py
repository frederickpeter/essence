from django.shortcuts import render
from .models import Gender, Brand,Category

# Create your views here.
def index(request):
    genders = Gender.objects.all().prefetch_related('categories')
    brands = Brand.objects.all()[:6]
    context = {'genders':genders, 'brands':brands}
    return render(request, 'shop/index.html', context)


def categories(request, slug):
    return render(request, "shop/shop.html")


def blogs(request):
    return render(request, "shop/blog.html")
