from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN-13 standard
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title