# **Authentication-and-User-Management-using-Django-Framework**
 

## **Table of Contents**
1. **Introduction**
2. **Project Setup**
3. **Configure VIEWS and URLS**
4. **Setup Postgres Database**
5. **Authentications**
6. **Work with User Management**
7. **Permissions**

### 1. Introduction
In this project i created a user account with logging functionality using Pythons Django Framework which contains an wide array of built in functionality designed to meet most needs of application designers. User activity was monitored from a locally hosted postgress database, they were abble to register, logging, reset, and change passwords.  
Authentication identifies and verifies the person trying to access an account by comparing with previous collected digital information, varification aims to validate the information provided.  

#### Tools Used : Django 3.0, Python 3.10, Crispy forms, Boostrap5, psycopg2

### 2. Project Setup
A virtual enviroment that creates an isolated enviroment for dependancies was created to ensure modules have the correct versions downloaded. 
```console
$ python -m venv myvenv
$ source venv/bin/activate
(venv) $ python -m pip install --upgrade pip
(venv) $ python -m pip install django
(venv) $ python -m pip install psycopg2
(venv) $ python -m pip install crispy-bootstrap5
(venv) $ python -m pip install crispy-forms
```

With all dependancies installed successfully, a new application, main, was created and installed by adding it together with others in the INSTALLED_APPS. 
```Python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # New applications
    'main.apps.MainConfig',     
    'crispy_forms',
    'crispy_bootstrap5',
]
```

### 3.Configure VIEWS and URLS
Views are python functions that are part of the user interface, they render pages on a web browser by taking requests and returning responses. They are hosted inside views.py file inside the main application folder. Contents inside were replaced with this code ;

```Python
from django.shortcuts import render

# A function based view that returns the home template
def home(request):
    # take the request and render home template 
    return render(request, 'main/home.html')
```
A new file urls.py inside the same folder as above was created and a path() function added to the urlpatterns[] list with arguments that will route users to the home page.
Inside urls.py, the path object and views module were imported. 
```Python
from django.urls import path
from . import views

urlpatterns = [
    # Display the home function 
    path('', views.home, name='home'),
]
```
A html file to be rendered should was placed inside a template folder in the main app, two other subdirectories, main and registration were created inside it. The former will have html templates while the latter will contained authentication urls. 
The base template had all features in every html file, they include : a navigation bar, header etc were inherited by child templates. 

Base Template 
```Python
{% extends 'main/base.html' %}
{% block title %}Home Page{% endblock %} 
{% block content %}
<h1>Coles Home page</h1>
{% endblock %}
```

### 4. Setup Postgres Database
A self-hosting PostgreSQL database inside settings file was created and configured to hold user credentials. 
```Python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Authentications', # database name 
        'USER': 'postgres',  # Default database name
        'HOST': 'localhost',  
        'PASSWORD': '*******',  
        'PORT': '5432',  
    }
}
```
Finally, migrations were applied from the command line as follws ;
```console
py manage.py migrate
```

### 5.Authentication.
Django is extremely versatile with its resource rich modules. Authentication and permission functionality is inbuilt, developers utilize this feature in verifying users (or groups) credetials and define actions that they can undertake i.e password change, password reset, login and logout just to mention a few.   

First Django authenticated site address neccesary for user management such as logins and logouts is added to urls.py file inside the website folder. Its designed to automate our tasks by rendering specific templates. 

```Python
urlpatterns = [
    path('admin/', admin.site.urls),
    # base url routes to the views in the app. 
    path('', include('main.urls')),
    # pre-built authentication urls
    path('', include('django.contrib.auth.urls')),
]
```

For a log in page, login.html file is placed inside the registration folder and accessed directly via a route by extending the base template. 
```Python
{% extends 'main/base.html' %} 

{% block title %}Login{% endblock %} 

# Load crispy form
{% load crispy_forms_tags %} 

{% block content %}

<form method="post">
    # Security for all forms with method post 
  {% csrf_token %}{{form|crispy}}
  # If user doesn't have an account click here to create one 
  <p>Dont have an account? Create one <a href="/sign-up">Here</a>!</p>
  # Button to submit form 
  <button type="submit" class="btn btn-success">Login</button>
</form>

{% endblock %}
```

Inside the main app urls file we added a route that will redirect user to the home base url when they click the home tab in the log in page.
```Python
urlpatterns = [
    # directs users to a home page
    path('', views.home, name='home'), 
    path('home/', views.home, )
]
```

Boostrap5 must be added to the settings file so as to use its features in customising forms.  
```Python
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# login and logout variables
LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/login'

```


