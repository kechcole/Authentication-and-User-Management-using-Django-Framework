from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
# Login and logouts 
from django.contrib.auth import login, logout, authenticate
# import Decorators 
from django.contrib.auth.decorators import login_required, permission_required
# import model to be queried 
from .models import Post


# Create your views here.
# Define a function based view that returns the home template
@login_required(login_url="/login")   # Add login url 
def home(request):
    # Query database , this variable is accessed by for loop in home page
    posts = Post.objects.all()

    # Create form for delete button in home template
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        user_id = request.POST.get("user-id")
        # print(f"post id : {post_id}  while user id : {user_id} and post : {post.author}")
        
        # Delete post if user is the author of post request
        # Add a nother condition so that user in mod group can delete post 
        if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
            post.delete()




    # take the request and render home template in the app folder
    return render(request, 'main/home.html', {"userposts": posts})



# Define a view for posts the renders a create_form html.
@login_required(login_url="/login")  # login decorator user must login. 
# Permission to add post 
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        # If request is a POST , capture the data that is title and description
        form = PostForm(request.POST)
        if form.is_valid():
            # Do not commit the data first because we dont have the user name 
            post = form.save(commit=False)
            # Get user name and then save form data 
            post.author = request.user
            post.save()   # Add to database , commit is True by default
            return redirect("/home")
    else:
        form = PostForm()   # Empty form

    return render(request, 'main/create_post.html', {"form": form})



# Sing up view function
def sign_up(request):
    # Request is POST
    if request.method == 'POST':
        # create and populate a register form and pass post data to them, then it will  
        # automatically validate the data an be rendered.
        # The form is located in form.py
        form = RegisterForm(request.POST)
        # validate form
        if form.is_valid():
            user = form.save()   # Create user and save user informtion 
            login(request, user)    # Log in user by passing requets and user data
            # After signing user redirect him to the home page. 
            return redirect('/home')
        
    # Request is GET
    else:
        # Create an empty form 
        form = RegisterForm()

    # Pass the form data to page to be displayed
    return render(request, 'registration/sign_up.html', {"form": form})