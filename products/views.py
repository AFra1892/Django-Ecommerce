from django.shortcuts import render
from .forms import ProductForm
# Create your views here.
from django.shortcuts import render , redirect
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

def product_create_view(request):
    form = ProductForm(request.POST or None)
    context = {"form":form}

    if form.is_valid():
        obj =form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('product-list')

    return render(request , "products/create.html" , context)