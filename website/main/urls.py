from django.urls import path
from . import views   # import all everything from current folder

urlpatterns = [
    # Display the views.home function , directs users to a home page
    path('', views.home, name='home'),
    # When user clicks home tab in login page 
    path('home/', views.home, name='home'),
    # Sign up route 
    path('sign-up/', views.sign_up, name='sign_up'),
    # Create post route 
    path('create-post/', views.create_post, name='create_post'),
]