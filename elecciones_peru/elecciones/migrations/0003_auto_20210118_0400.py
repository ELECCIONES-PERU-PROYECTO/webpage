# Generated by Django 3.1.5 on 2021-01-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0002_auto_20210117_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='apellido_materno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='apellido_paterno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='cargo_postula',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='carnet_extranjeria',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='dni',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='fecha_nacimiento',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='l_d_direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='l_d_distrito',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='l_n_distrito',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='link_foto',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='nombres',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='org_politica_postulate',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='ExperienciaLaboral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro_laboral', models.CharField(max_length=300)),
                ('oficio', models.CharField(max_length=400)),
                ('ruc_empresa_laboral', models.CharField(max_length=30)),
                ('direccion_laboral', models.CharField(max_length=100)),
                ('desde', models.CharField(max_length=20)),
                ('hasta', models.CharField(max_length=20)),
                ('pais_laboral', models.CharField(max_length=80)),
                ('departamento_laboral', models.CharField(max_length=80)),
                ('provincia_laboral', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'experiencia_laboral',
                'unique_together': {('ruc_empresa_laboral', 'desde', 'hasta')},
            },
        ),
    ]