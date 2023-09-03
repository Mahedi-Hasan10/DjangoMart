from django.shortcuts import render,redirect
from .models import Cart, CartItem
from store.models import Product
# Create your views here.
def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key
def cart(request):
    cart_items = None
    total = 0
    tax = 0
    grand_total =0
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user = request.user)
        for item in cart_items:
            total += item.product.price*item.quantity
    
    else:
        session_id = get_create_session(request)
        cart = Cart.objects.get(cart_id=session_id)
        cart_id = Cart.objects.filter(cart_id=session_id).exists()
        
        if cart_id:
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                total += item.product.price*item.quantity
    
    tax = (total*2)/100
    grand_total = tax+total
    
    context = {
        'items':cart_items,
        'total':total,
        'tax':tax,
        'grand_total':grand_total
    }
    return render(request,'cart/cart.html',context)

def add_to_cart(request,product_id):
    product = Product.objects.get(id = product_id)
    session_id = get_create_session(request)
    
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(product=product,user=request.user).exists()
        if cart_item:
            item = CartItem.objects.get(product=product)
            item.quantity += 1
            item.save()
        else:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                user = request.user,
            
            )
            cart_item.save() 
    else:   
        cartId = Cart.objects.filter(cart_id=session_id).exists()
        if cartId:
            cart_item = CartItem.objects.filter(product=product).exists()
            if cart_item:
                item = CartItem.objects.get(product=product)
                item.quantity += 1
                item.save()
            else:
                cartId = Cart.objects.get(cart_id=session_id)
                cart_item = CartItem.objects.create(
                    product = product,
                    cart = cartId,
                    quantity = 1)
                cart_item.save()       
        else:    
            cart = Cart.objects.create(
                cart_id = session_id
            )
            cart.save()
            cartId = Cart.objects.get(cart_id=session_id)
            cart_item = CartItem.objects.create(
                product = product,
                cart = cartId,
                quantity = 1)
            cart_item.save()      
    return redirect('cart')

def remove_cart_item(request,product_id):
    product = Product.objects.get(id=product_id)
    session_id = get_create_session(request)
    if request.user.is_authenticated:
        cartItem = CartItem.objects.get(product=product,user=request.user)
        if cartItem.quantity > 1:
            cartItem.quantity -= 1
            cartItem.save()
        else:
            cartItem.delete()
    else:    
        cartId = Cart.objects.get(cart_id = session_id)
        if cartId:
            cartItem = CartItem.objects.get(cart=cartId,product=product)
            # print(cartItem)
            if cartItem.quantity > 1:
                cartItem.quantity -= 1
                cartItem.save()
            else:
                cartItem.delete()
    return redirect('cart')

def remove_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        cartItem = CartItem.objects.get(product=product,user=request.user)
        cartItem.delete()
    else:
        session_id =get_create_session(request)
        cartId = Cart.objects.get(cart_id = session_id)
        if cartId:
            cartItem = CartItem.objects.get(cart=cartId,product=product)
            cartItem.delete()
    return redirect('cart')


