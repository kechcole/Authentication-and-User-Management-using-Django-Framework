from django.db import models
# Import user 
from django.contrib.auth.models import User  

# Create your models here.
# A model for user post
class Post(models.Model):
    # Pass a user object, links our post to a specific author so we can access 
    # their name and other properties  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Title of post
    title = models.CharField(max_length=200)      
    # Additional information
    description = models.TextField() 
     # Date created , once instance of an object is added    
    created_at = models.DateTimeField(auto_now_add=True) 
    # Date modified , update field when save metod is called 
    updated_at = models.DateTimeField(auto_now=True) 
     
    # Display the tiltle and description
    def __str__(self):
        return self.title + "\n" + self.description
