from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import status
from books.serializers import BookSerializer
from books.models import Book
from users.mixins import CustomPermissionMixin


# Create your views here.


class BooksListApiView(ListAPIView):
        model = Book
        queryset = Book.objects.all()
        serializer_class = BookSerializer


class BookCreateApiView(CustomPermissionMixin, CreateAPIView):
        model = Book
        queryset = Book.objects.all()
        serializer_class = BookSerializer


class BookUpdateApiView(CustomPermissionMixin,UpdateAPIView):
        model = Book
        queryset = Book.objects.all()
        serializer_class = BookSerializer


class BookDeleteApiView(CustomPermissionMixin,DestroyAPIView):
        model = Book
        queryset = Book.objects.all()
        serializer_class = BookSerializer

class BookRetrieveApiView(CustomPermissionMixin,RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def index(request):
        return JsonResponse({'message':"успешно подключено"},status=status.HTTP_200_OK)