# Generated by Django 3.1.7 on 2021-03-09 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0002_auto_20210309_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablaedad',
            old_name='dni_candidato',
            new_name='dni',
        ),
    ]