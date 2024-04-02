from django.contrib import admin
from .models import Gender, Brand, Category, ProductType, GlobalDiscount, Product

# Register your models here.
admin.site.register(Gender)

admin.site.register(Brand)

admin.site.register(Category)

admin.site.register(ProductType)

admin.site.register(GlobalDiscount)

admin.site.register(Product)
