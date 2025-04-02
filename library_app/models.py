from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN-13 standard but unique
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}" # to return the title and the author of the book
    
class LibraryUser(AbstractUser):
    date_of_membership = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username