from django import template

register = template.Library()

@register.filter
def product_in_cart(product, cart_items):
    """
    Custom template filter to check if a product exists in the cart items.
    """
    return cart_items.filter(product=product).exists()
