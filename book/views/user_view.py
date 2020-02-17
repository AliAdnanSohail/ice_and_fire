from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from book.serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_obj = user_serializer.save()
        user_token = Token.objects.create(user=user_obj)
        formatted_response = {'data': user_serializer.data, 'token': user_token.key}
        return Response(formatted_response, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sign_in(request):
    username = request.data.get('username')
    password = make_password(request.data.get('password'))
    user_obj = get_object_or_404(User, username=username, password=password)
    serialized_data = UserSerializer(user_obj)
    (token, is_new_created) = Token.objects.get_or_create(user=user_obj)
    formatted_response = {'data': serialized_data.data, 'token': token.key}
    return Response(formatted_response)
