# Generated by Django 4.0.4 on 2023-04-22 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0004_alter_curso_comision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='comision',
            field=models.IntegerField(),
        ),
    ]