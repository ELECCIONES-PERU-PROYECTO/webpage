# Generated by Django 3.1.5 on 2021-01-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentenciapenal',
            name='fallo_penal',
            field=models.CharField(max_length=300),
        ),
    ]