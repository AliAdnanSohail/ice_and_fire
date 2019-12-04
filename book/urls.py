from django.urls import path
from book.views.external_book_view import ExternalBookList
from book.views.book_view import BookListCreateView, BookRetrieveUpdateDestroyView
from book.views.country_view import CountryListView
from book.views.user_view import signup, sign_in

urlpatterns = [
    path('external-books/', ExternalBookList.as_view(), name='external-book-list'),
    path('books/', BookListCreateView.as_view(), name='books-all'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('countries/', CountryListView.as_view(), name='countries-all'),
    path('user/signup', signup, name='user-signup'),
    path('user/sign_in', sign_in, name='user-sign_in')
]
