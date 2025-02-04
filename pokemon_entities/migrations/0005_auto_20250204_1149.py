# Generated by Django 3.1.14 on 2025-02-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время появления'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='disapeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время исчезновения'),
        ),
    ]
