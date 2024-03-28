from django.shortcuts import render

# Create your views here.



from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count
from .models import Travel, Country
from .serializers import TravelSerializer, CountrySerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.annotate(travel_count=Count('travels'))
    serializer_class = CountrySerializer