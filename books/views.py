from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from books.serializers import BookSerializer
from books.models import Book

# Create your views here.


class BooksListApiView(ListAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(CreateAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(DestroyAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer