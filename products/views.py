from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list_view(request):
    product_list = Product.objects.all()
    context = {"object_list":product_list}
    return render(request , "products/list.html" , context)

def product_detail_view(request , id):
    product = Product.objects.get(id=id)
    context = {"object":product}
    return render(request , "products/detail.html" , context)