from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page of the store
    path('products/', views.products, name='products'),  # Products page of the store
    path('contact/', views.contact, name='contact'),  # Contact page of the store
    path('about/', views.about, name='about'),  # About page of the store
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Register page of the store
    path('cart/', views.cart, name='cart'),  # Cart page of the store
] 
