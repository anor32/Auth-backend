from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView

from books.serializers import BookSerializer
from books.models import Book

# Create your views here.


class ListBooks(ListAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer