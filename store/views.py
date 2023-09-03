from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator
# Create your views here.
def store(request,category_slug=None):
    products = None
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = category)
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True)
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)

        
    categories = Category.objects.all()
    context ={
        'products':paged_product,
        'categories':categories
    }
    return render(request,'store/store.html',context)
def product_detail(request,category_slug,product_slug):
    single_product = Product.objects.get(slug=product_slug, category__slug = category_slug)
    return render(request,'store/product-detail.html',{'product':single_product})