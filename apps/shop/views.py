from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def categories(request, pk):
    return render(request, "shop/shop.html")


def blogs(request):
    return render(request, "shop/blog.html")
