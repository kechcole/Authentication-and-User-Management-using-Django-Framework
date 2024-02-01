from django import forms
from django.contrib.auth.forms import UserCreationForm  # Django form
# Where to store User models
from django.contrib.auth.models import User
from .models import Post


# Class based form created by extending the Django's form
class RegisterForm(UserCreationForm):
    # By default email field is not provided so we must design other include date, image, boolean
    # This field must not be left blank or given a None value
    email = forms.EmailField(required=True)

    # Create a user in the form
    class Meta:
        model = User
        # Fields needed from the user model 
        fields = ["username", "email", "password1", "password2"]

# Class based form for Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Fields to be filled in by user.
        fields = ["title", "description"]