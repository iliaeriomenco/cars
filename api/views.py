from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Car, Driver
from .serializers import CarSerializer, DriverSerializer


class CarViewSet(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarSerializer
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		import ipdb;ipdb.set_trace()
		serializer.save(added_by=self.request.user)


class DriverViewSet(viewsets.ModelViewSet):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer
	permission_classes = (IsAuthenticated,)
