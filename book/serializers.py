from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework import serializers
from book.models.book import Book, Author, Country
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        print(validated_data["password"], "is the password")
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    country = CountrySerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        country = validated_data.pop('country')
        country = Country.objects.filter(name=country["name"]).first()
        if not country:
            exception_string = 'Country does not exists, please goto {url} to see all countries'\
                                .format(url=reverse('countries-all'))
            raise ObjectDoesNotExist(exception_string)

        validated_data['country_id'] = country.id
        book = Book.objects.create(**validated_data)
        for author in authors:
            author_obj = Author.objects.filter(name=author['name']).first()
            if not author_obj:
                author_obj = Author.objects.create(name=author['name'])
                author_obj.save()
            book.authors.add(author_obj)
        return book

    def update(self, book_instance, validated_data):
        if validated_data.get('country'):
            country = validated_data.pop('country')
            country = Country.objects.filter(name=country["name"]).first()
            if not country:
                raise ObjectDoesNotExist('Country does not exists')
            validated_data['country_id'] = country.id

        if validated_data.get('authors'):
            authors = validated_data.pop('authors')
            book_instance.authors.clear()
            for author in authors:
                author_obj = Author.objects.filter(name=author['name']).first()
                if not author_obj:
                    author_obj = Author.objects.create(name=author['name'])
                    author_obj.save()
                book_instance.authors.add(author_obj)

        for key, value in validated_data.items():
            setattr(book_instance, key, value)

        book_instance.save()
        return book_instance

