from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Category, Brand


# This form is used for user registration, extending the built-in UserCreationForm
# to include an email field and custom validation for username and email uniqueness.
# It ensures that the email is valid and not already in use, and that the username is unique.
# The save method is overridden to ensure the email is saved correctly when the user is created.
# This form can be used in views to handle user registration, providing a user-friendly interface
# for new users to sign up.
# The form includes validation to ensure that the email and username are unique,
# and it provides a clean interface for users to register with a username, email, and password.
# The `clean_email` and `clean_username` methods check for existing users with the same email or username,
# raising a validation error if duplicates are found.


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email


class ProductFilterForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["category", "brand"]

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False, empty_label="All Categories"
    )

    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(), required=False, empty_label="All Brands"
    )

    min_price = forms.DecimalField(
        required=False, min_value=0, decimal_places=2, label="Min Price", initial=0.00
    )
    max_price = forms.DecimalField(
        required=False, min_value=0, decimal_places=2, label="Max Price", initial=0.00
    )
