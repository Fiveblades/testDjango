# Generated by Django 5.0.1 on 2024-01-31 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voetballer_naam', models.CharField(max_length=100)),
                ('voetbalclub', models.CharField(max_length=100)),
                ('auteur_naam', models.CharField(max_length=100)),
                ('datum_invoer', models.DateTimeField(auto_now_add=True)),
                ('datum_wijziging', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
