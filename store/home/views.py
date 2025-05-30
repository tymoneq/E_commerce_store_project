from django.shortcuts import render
from .models import Product

def index(request):
    """
    Render the index page of the store.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered index page.
    """
    return render(request, 'home/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {'products': products})