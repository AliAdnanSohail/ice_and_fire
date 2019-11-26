from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from book.services.ice_and_fire_service import IceAndFireService


class ExternalBookList(APIView):
    def get(self, request):
        ice_and_fire_obj = IceAndFireService()
        status_code, all_books = ice_and_fire_obj.get_all_books(query_params=request.query_params)
        formatted_response = {'data': all_books, 'status_code': status_code, 'status': 'success'}
        return Response(formatted_response, status=status.HTTP_200_OK)
