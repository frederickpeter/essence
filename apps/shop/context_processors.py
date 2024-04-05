from .models import Gender, CartItem



def gender_and_categories(request):
    return {
        "genders": Gender.objects.all().prefetch_related('categories')
    }

def cart_items(request):
    items = CartItem.objects.filter(cart__user__id=2)
    return {
        'cart_items': items,
        'total_cart_items':items.count()
    }