from rest_framework import serializers
from django.contrib.auth.models import User

# User = get_user_model(settings.AUTH_USER_MODEL)
from .models import Car, Driver

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'username', 'id', 'is_staff',
			'first_name', 'last_name', 'email'
		)


class CarSerializer(serializers.ModelSerializer):
	added_by = UserSerializer(read_only=True)

	class Meta:
		model = Car
		fields = '__all__'

	def create(self, validated_data):
		instance = Car(**validated_data)
		instance.save()
		return instance


class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = '__all__'
