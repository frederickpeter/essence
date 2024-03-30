from typing import Iterable
from django.db import models
from django.utils.text import slugify

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
    MEN = "Men's"
    WOMEN = "Women's"
    KID = "Kid's"

    genders = {
        MEN:"Men's",
        WOMEN:"Women's",
        KID: "Kids's"
    }

    name = models.CharField(max_length=10, choices=genders, default=MEN, unique=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='categories')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.gender} - {self.name}"
    
    class Meta:
        verbose_name_plural = "categories"
        unique_together = ['name', 'gender']