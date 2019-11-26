from django.urls import path
from book.views.external_book_view import ExternalBookList
from book.views.book_view import BookListCreateView, BookRetrieveUpdateDestroyView
from book.views.country_view import CountryListView

urlpatterns = [
    path('external-books/', ExternalBookList.as_view(), name='external-book-list'),
    path('books/', BookListCreateView.as_view(), name='books-all'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('countries/', CountryListView.as_view(), name='countries-all'),
]
