from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),  # Home page of the store
    path("products/", views.products, name="products"),  # Products page of the store
    path("contact/", views.contact, name="contact"),  # Contact page of the store
    path("about/", views.about, name="about"),  # About page of the store
    path("profile/", views.profile, name="profile"),  # Profile page of the store
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="home/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register, name="register"),  # Register page of the store
    path("cart/", views.view_cart, name="view_cart"),  # Cart page of the store
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("checkout/", views.checkout, name="checkout"),  # Checkout page of the store
    path("order-success/<int:order_id>/", views.order_success, name="order_success"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
]
