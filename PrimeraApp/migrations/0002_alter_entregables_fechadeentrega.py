# Generated by Django 4.0.4 on 2023-04-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregables',
            name='fechaDeEntrega',
            field=models.DateField(max_length=20),
        ),
    ]