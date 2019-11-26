import requests


class IceAndFireService:
    API_URL = 'https://www.anapioficeandfire.com/api/books'

    def get_all_books(self, query_params):
        response = requests.get(url=self.API_URL, params=query_params)
        status_code, all_books = response.status_code, response.json()
        all_books = [self.format_book_data(book) for book in all_books]
        return status_code, all_books

    def format_book_data(self, book):
        return {'name': book['name'],
                'isbn': book['isbn'],
                'authors': book['authors'],
                'number_of_pages': book['numberOfPages'],
                'publisher': book['publisher'],
                'country': book['country'],
                'release_date': book['released']
                }

