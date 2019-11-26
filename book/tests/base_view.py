from rest_framework.test import APITestCase, APIClient
from book.models.book import Book, Author


class BaseViewTest(APITestCase):
    client = APIClient()
    @staticmethod
    def create_book(name, authors, publisher, country, release_date, isbn):
        book = Book.objects.create(name=name, publisher=publisher,
                                   country=country, release_date=release_date, isbn=isbn)
        for a in authors:
            author = Author.objects.filter(name=a['name']).first()
            if not author:
                author = Author.objects.create(name=a['name'])
                author.save()
            book.authors.add(author)

    def setUp(self):
        self.create_book(name='book_name1', authors=[{'name': 'author1'}, {'name': 'author2'}],
                         publisher='publisher1', country='country1', release_date='2010-10-10', isbn='isbn1')
        self.create_book(name='book_name2', authors=[{'name': 'author1'}, {'name': 'author2'}],
                         publisher='publisher2', country='country2', release_date='2010-10-10', isbn='isbn2')
        self.create_book(name='book_name3', authors=[{'name': 'author1'}, {'name': 'author2'}],
                         publisher='publisher3',country='country3', release_date='2015-10-10', isbn='isbn3')
