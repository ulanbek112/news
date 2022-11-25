from django.shortcuts import render
from rest_framework import generics

from main.models import News, Register
from main.serializer import NewsSerializer, RegisterSerializer


class NewsAPIList(generics.ListCreateAPIView):
    queryset =  News.objects.all()
    serializer_class = NewsSerializer

class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset =  News.objects.all()
    serializer_class = NewsSerializer

class NewsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset =  News.objects.all()
    serializer_class = NewsSerializer

class RegisterAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Register.objects.all()
    serializer_class = RegisterSerializer

class RegisterAPIList(generics.ListCreateAPIView):
    queryset =  Register.objects.all()
    serializer_class = RegisterSerializer