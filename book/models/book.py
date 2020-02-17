from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)
    isbn = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, related_name="book_list")
    number_of_pages = models.PositiveIntegerField(default=0)
    publisher = models.CharField(max_length=200)
    country = models.ForeignKey('book.country', on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return '{name} By {publisher}'.format(name=self.name, publisher=self.publisher)


class Country(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
