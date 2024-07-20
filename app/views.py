from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import Userserializer,Bookserializer,Issuebookserializer
# Create your views here.

class userapi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class bookapi(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class issuebook(generics.CreateAPIView):
    queryset = Issuebook.objects.all()
    serializer_class = Issuebookserializer