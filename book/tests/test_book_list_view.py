from rest_framework import status
from django.urls import reverse
from ice_and_fire_api.book.models.book import Book
from ice_and_fire_api.book.serializers import BookSerializer
from .base_view import BaseViewTest


class AllBooksTest(BaseViewTest):
    def test_get_all_books(self):
        """
        This test to check endpoint is returning all books
        """
        response = self.client.get(reverse('books-all'))
        expected = Book.objects.all()
        serialized = BookSerializer(expected, many=True)
        self.assertEqual(response.data['data'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')

    def test_create_book(self):
        """
        This test to check post request is creating new book
        """
        book = {
            "name": "test_name3",
            "isbn": "isbn",
            "number_of_pages": 250,
            "publisher": "test_publisher",
            "country": "test_country",
            "release_date": "2016-02-02",
            "authors": [
                {"name": "auth1"},
                {"name": "auth2"}
            ]
        }
        response = self.client.post(reverse('books-all'), book)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status_code'], status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['name'], book['name'])
        self.assertEqual(response.data['data']['authors'], book['authors'])

    def test_filter_books(self):
        """
        This test to check endpoint is filtering books on base of country, name, year of publication
        and publisher
        """
        search_str = 'book_name1'
        url = '{url}?search={search}'.format(url=reverse('books-all'), search=search_str)
        response = self.client.get(url)
        expected_book = Book.objects.get(name=search_str)
        serialized = BookSerializer(expected_book)
        self.assertEqual(serialized.data['id'], response.data['data'][0]['id'])

        search_str = 'country2'
        url = '{url}?search={search}'.format(url=reverse('books-all'), search=search_str)
        response = self.client.get(url)
        expected_book = Book.objects.get(country=search_str)
        serialized = BookSerializer(expected_book)
        self.assertEqual(serialized.data['id'], response.data['data'][0]['id'])

        search_str = '2015'
        url = '{url}?search={search}'.format(url=reverse('books-all'), search=search_str)
        response = self.client.get(url)
        expected_book = Book.objects.get(release_date__year=search_str)
        serialized = BookSerializer(expected_book)
        self.assertEqual(serialized.data['id'], response.data['data'][0]['id'])

        search_str = 'publisher3'
        url = '{url}?search={search}'.format(url=reverse('books-all'), search=search_str)
        response = self.client.get(url)
        expected_book = Book.objects.get(publisher=search_str)
        serialized = BookSerializer(expected_book)
        self.assertEqual(serialized.data['id'], response.data['data'][0]['id'])


