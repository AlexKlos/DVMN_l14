# Generated by Django 3.1.14 on 2025-02-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20250204_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='Strength',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Сила'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Защита'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Здоровье'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Уровень'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Выносливость'),
        ),
    ]
