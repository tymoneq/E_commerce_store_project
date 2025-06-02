from django.shortcuts import render
from .models import Product
from .forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    return render(request, 'home/home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'home/products.html', {'products': products})

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def login(request):
    return render(request, 'home/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'home/register.html', {'form': form})

def cart(request):
    return render(request, 'home/cart.html')