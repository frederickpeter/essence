from django.contrib import admin
from .models import (
    Gender,
    Brand,
    Category,
    ProductType,
    GlobalDiscount,
    Product,
    Cart,
    CartItem,
)

# Register your models here.
admin.site.register(Gender)

admin.site.register(Brand)

admin.site.register(Category)

admin.site.register(ProductType)

admin.site.register(GlobalDiscount)

admin.site.register(Product)

admin.site.register(Cart)

admin.site.register(CartItem)
