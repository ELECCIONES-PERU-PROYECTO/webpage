# Generated by Django 3.1.5 on 2021-01-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0003_auto_20210119_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentenciaobligacion',
            name='fallo_obliga',
            field=models.CharField(max_length=500),
        ),
    ]
