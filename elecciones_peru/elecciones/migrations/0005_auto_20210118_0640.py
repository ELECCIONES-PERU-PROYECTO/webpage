# Generated by Django 3.1.5 on 2021-01-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0004_auto_20210118_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='sexo',
            field=models.CharField(max_length=10),
        ),
    ]
