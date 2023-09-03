from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from cart.models import Cart, CartItem
def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key
# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
    return render(request,'accounts/register.html',{'form':form})
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'accounts/dashboard.html')
def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username,password=password
                            )
        session_key = get_create_session(request)
        cart = Cart.objects.get(cart_id=session_key)
        is_items_exists = CartItem.objects.filter(cart=cart).exists()
        if is_items_exists:
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                item.user = user
                item.save()
        login(request,user)
        return redirect('profile')
        
    return render(request,'accounts/signin.html')
def user_logout(request):
    logout(request)
    return redirect('login')