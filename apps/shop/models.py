from django.db import models
from django.utils.text import slugify
from functools import partial
from apps.utils.upload import unique_file_name_generator
from django.utils import timezone

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Gender(models.Model):
    MEN = "men"
    WOMEN = "women"
    KID = "kid"

    genders = {MEN: "Men", WOMEN: "Women", KID: "Kid"}

    name = models.CharField(max_length=10, choices=genders, default=MEN, unique=True)

    def __str__(self) -> str:
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to=partial(unique_file_name_generator, base_path="product-types"),
        help_text="Background image of product type - ideal resolution of 800x533",
    )

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.CASCADE, related_name="categories"
    )
    type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, related_name="categories"
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.gender} - {self.name}"

    class Meta:
        verbose_name_plural = "categories"
        unique_together = ["name", "gender"]


class GlobalDiscount(models.Model):
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.discount_rate}%"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    @property
    def discounted_price(self):
        if self.discount_rate:
            discounted_price = self.base_price * (1-self.discount_rate / 100)
            return discounted_price
        else:
            cur_date = timezone.now()
            global_discount = GlobalDiscount.objects.filter(start_date__lte=cur_date, end_date__gte=cur_date).first()
            if global_discount:
                discount_rate = global_discount.discount_rate
                discounted_price = self.base_price * (1 - discount_rate / 100)
                return discounted_price
            else:
                return self.base_price
            
    
    def __str__(self) -> str:
        return self.name