from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import UserRegistrationForm, ProductFilterForm
from django.contrib import messages


def home(request):
    return render(request, "home/home.html")


def products(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data["category"]:
            products = products.filter(category=form.cleaned_data["category"])
        if form.cleaned_data["brand"]:
            products = products.filter(brand=form.cleaned_data["brand"])

        if form.cleaned_data["min_price"] is not None:
            products = products.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"] is not None:
            products = products.filter(price__lte=form.cleaned_data["max_price"])

    return render(request, "home/products.html", {"products": products, "form": form})


def contact(request):
    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")


def profile(request):
    if request.method == "POST":
        # Handle profile update logic here
        messages.success(request, "Profile updated successfully!")
    return render(request, "home/profile.html")


def login(request):
    return render(request, "home/login.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "home/register.html", {"form": form})


def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})

    if isinstance(product_id, int):
        product_id = str(product_id)
    if str(product_id) not in cart:
        # If product_id is not in the cart, add it with quantity 1
        cart[product_id] = 1
    else:
        cart[product_id] += 1
    request.session["cart"] = cart
    messages.success(request, "Product added to cart!")
    return redirect("products")  # or wherever you want to go


def view_cart(request):
    cart = request.session.get("cart", {})  # {product_id: quantity}

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    cart_items = []
    total_price = 0

    for product in products:
        quantity = cart.get(str(product.id)) or cart.get(product.id)
        subtotal = product.price * quantity
        total_price += subtotal

        cart_items.append(
            {
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            }
        )

    return render(
        request,
        "home/cart.html",
        {
            "cart_items": cart_items,
            "total_price": total_price,
        },
    )

@require_POST
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        del cart[str(item_id)]  # Remove product from session cart

    request.session['view_cart'] = cart
    return redirect('view_cart')  # Redirect to cart page


def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, "home/order_success.html", {"order": order})


@login_required
def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect("products")

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    total_price = 0
    order_items = []

    for product in products:
        quantity = cart.get(str(product.id)) or cart.get(product.id)
        subtotal = product.price * quantity
        total_price += subtotal
        order_items.append((product, quantity, product.price))

    # Create order
    order = Order.objects.create(user=request.user, total_price=total_price)

    for product, quantity, price in order_items:
        OrderItem.objects.create(
            order=order, product=product, quantity=quantity, price=price
        )

    # Clear cart
    request.session["cart"] = {}
    messages.success(request, "Checkout successful! Your order has been placed.")

    return redirect("order_success", order_id=order.id)
