from django.urls import path
from books.apps import BooksConfig
from books.views import BooksListApiView, BookCreateApiView, BookUpdateApiView, BookDeleteApiView, BookRetrieveApiView

app_name = BooksConfig.name
urlpatterns = [
    path('books/', BooksListApiView.as_view(), name='books_list'),
    path('books/create/', BookCreateApiView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view(), name='book_update'),
    path('books/<int:pk>/detail/', BookRetrieveApiView.as_view(), name='book_detail'),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), name='book_delete'),
]