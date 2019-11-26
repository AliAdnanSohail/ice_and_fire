from rest_framework import generics, status, filters
from rest_framework.response import Response
from book.models.book import Book
from book.serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country', 'publisher', 'release_date']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        formatted_response = {'data': response.data, 'status': 'success', 'status_code': status.HTTP_200_OK}
        return Response(formatted_response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        formatted_response = {'data': response.data, 'status': 'success', 'status_code': status.HTTP_201_CREATED}
        return Response(formatted_response, status=status.HTTP_201_CREATED)


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        formatted_response = {'data': response.data, 'status': 'success', 'status_code': status.HTTP_200_OK}
        return Response(formatted_response, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        message = 'The book {name} was updated successfully'.format(name=response.data['name'])
        formatted_response = {'data': response.data, 'status': 'success',
                              'message': message, 'status_code': status.HTTP_200_OK}
        return Response(formatted_response, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        response = super().delete(request, *args, **kwargs)
        message = 'The book {name} was deleted successfully'.format(name=book.name)
        formatted_response = {'data': response.data, 'status': 'success',
                              'message': message, 'status_code': status.HTTP_204_NO_CONTENT}
        return Response(formatted_response, status=status.HTTP_204_NO_CONTENT)
