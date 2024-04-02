from django.shortcuts import render
from .models import Gender, Brand, ProductType, GlobalDiscount, Product
from django.utils import timezone


# Create your views here.
def index(request):
    brands = Brand.objects.all()[:6]
    types = ProductType.objects.all()
    cur_date = timezone.now()
    discount = GlobalDiscount.objects.filter(
        start_date__lte=cur_date, end_date__gte=cur_date
    ).first()
    products = Product.objects.filter(quantity__gt=0)[:10]
    context = {
        "brands": brands,
        "types": types,
        "discount_rate": discount,
        "products": products,
    }

    return render(request, "shop/index.html", context)


def all_products(request):
    return render(request, "shop/products.html")


def type_products(request, name):
    return render(request, "shop/products.html")


def category_products(request, gender, slug):
    return render(request, "shop/shop.html")


def blogs(request):
    return render(request, "shop/blog.html")

def contect(request):
    return render(request, 'shop/contact.html')
