# Generated by Django 3.1.5 on 2021-01-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0006_auto_20210118_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='carnet_extranjeria',
            field=models.CharField(default='-', max_length=12),
        ),
    ]
