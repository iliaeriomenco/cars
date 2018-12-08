# Generated by Django 2.1.4 on 2018-12-07 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер')),
                ('car_model', models.CharField(max_length=40, verbose_name='Марка машины')),
                ('producer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Машина',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Водитель',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cars', to='api.Driver', verbose_name='Водитель'),
        ),
    ]
