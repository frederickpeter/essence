from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import (
    Gender,
    Brand,
    ProductType,
    GlobalDiscount,
    Product,
    Category,
    Cart,
    CartItem,
)
from django.utils import timezone
from django.db.models import Prefetch
from django.db.models import Max, Min
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here.
def index(request):
    brands = Brand.objects.all()[:6]
    types = ProductType.objects.all()[:3]
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
    # Number of items per page
    items_per_page = 10
    page_number = request.GET.get("page", 1)
    title = request.GET.get("type", None)
    category = request.GET.get("category", None)

    # Get the existing query parameters
    params = request.GET.copy()
    # Remove the 'page' parameter if it exists
    if "page" in params:
        del params["page"]
    # Construct the URL for pagination links with the existing query parameters
    base_url = reverse(
        "shop:all-products"
    )  # Replace 'your_view_name' with the name of your view
    query_string = params.urlencode()
    pagination_url = f"{base_url}?{query_string}&page="

    brands = Brand.objects.all()[:6]
    types = ProductType.objects.prefetch_related(
        Prefetch("categories", queryset=Category.objects.distinct("name"))
    )

    if title.lower() == "all products":
        products = Product.objects.all()
    elif title.lower() in ["clothing", "accessories", "shoes"]:
        if category is not None:
            products = Product.objects.filter(
                category__type__name__iexact=title, category__name__iexact=category
            )
        else:
            products = Product.objects.filter(category__type__name__iexact=title)
    elif title.lower() in ["men", "women", "kid"]:
        products = Product.objects.filter(
            category__gender__name__iexact=title, category__name__iexact=category
        )

    # Create a Paginator instance
    paginator = Paginator(products, items_per_page)
    # Get the objects for the current page
    page_objects = paginator.get_page(page_number)
    total_product_count = page_objects.object_list.count()
    prices = page_objects.object_list.aggregate(
        min_price=Min("base_price"), max_price=Max("base_price")
    )

    context = {
        "title": title,
        "category": category,
        "brands": brands,
        "types": types,
        "products": page_objects,
        "product_count": total_product_count,
        "min_price": prices["min_price"],
        "max_price": prices["max_price"],
        "url": pagination_url,
    }
    return render(request, "shop/products.html", context)


def single_product(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "shop/single-product-details.html", {"product": product})


def blogs(request):
    return render(request, "shop/blog.html")


def contect(request):
    return render(request, "shop/contact.html")


def cart(request):
    return render(request, "shop/cart.html")


def checkout(request):
    return render(request, "shop/checkout.html")


def add_to_cart(request, product_id):
    obj, created = Cart.objects.get_or_create(defaults={"user_id": 2}, user_id=2)

    CartItem.objects.create(product_id=product_id, cart=obj)
    url = f"{reverse('shop:all-products')}?type=all+products"
    return redirect(url)


def remove_from_cart(request, product_id):
    obj = get_object_or_404(Cart, user_id=2)

    CartItem.objects.get(product_id=product_id, cart=obj).delete()
    url = f"{reverse('shop:all-products')}?type=all+products"
    return redirect(url)
