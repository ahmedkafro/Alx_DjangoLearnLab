from django.db import models
##from django.contrib.auth.models import User

# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class book(models.Model):    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    
    
class Library(models.Model):    
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(book)

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name