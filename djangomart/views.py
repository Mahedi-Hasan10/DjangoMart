from django.shortcuts import render
from store.models import Product
from category.models import Category
def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context ={
        'products':products,
    }
    return render(request,'index.html',context)
