from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PostSerializer
 
 
class PostList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PostSerializer

# Create your views here.
