from rest_framework import generics
from book.models.book import Country
from book.serializers import CountrySerializer


class CountryListView(generics.ListAPIView):
    model = Country
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
