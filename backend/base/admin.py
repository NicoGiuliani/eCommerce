from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "category",
        "description",
        "rating",
        "numReviews",
        "price",
        "countInStock",
        "createdAt",
        "_id",
    )


admin.site.register(Product, ProductAdmin)
