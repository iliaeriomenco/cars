from django.conf import settings
from django.dispatch import receiver

from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Car(models.Model):
	added_by = models.ForeignKey(User, verbose_name='кто добавил',
								related_name='cars', 
								on_delete=models.DO_NOTHING,
								null=True, blank=True)
	number = models.CharField('Номер', max_length=20)
	car_model = models.CharField('Марка машины', max_length=40)
	producer = models.CharField('Производитель', max_length=100,
								blank=True, null=True)
	driver = models.ForeignKey('Driver',
								on_delete=models.DO_NOTHING,
								blank=True, null=True,
								verbose_name='Водитель',
								related_name='cars')

	def __str__(self):
		return f'{self.car_model} {self.number}'

	class Meta:
		verbose_name = 'Машина'


class Driver(models.Model):
	first_name = models.CharField('Имя', max_length=40)
	last_name= models.CharField('Фамилия', max_length=40)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:
		verbose_name = 'Водитель'
	

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)