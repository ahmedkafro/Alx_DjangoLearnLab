from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


#class BookList(ListAPIView):
 ##   queryset = Book.objects.all()
 ##   serializer_class = BookSerializer
    
from rest_framework import generics , viewsets
#from .models import Book
#from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    
    
class BookViewSet(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
                           