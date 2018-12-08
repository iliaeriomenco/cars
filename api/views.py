from django.shortcuts import render
from rest_framework import viewsets

from .models import Car, Driver
from .serializers import CarSerializer, DriverSerializer


class CarViewSet(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarSerializer


class DriverViewSet(viewsets.ModelViewSet):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer

