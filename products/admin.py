from django.contrib import admin
from .models import Product,Category,Discount
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)