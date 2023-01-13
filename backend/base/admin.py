from django.contrib import admin
from .models import *

# Register your models here.
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "brand",
#         "category",
#         "description",
#         "rating",
#         "numReviews",
#         "price",
#         "countInStock",
#         "createdAt",
#         "_id",
#     )


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
