from django.contrib import admin

from .models import Pokemon, PokemonEntity


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('pokemon', 'latitude', 'longitude', 'appeared_at', 'disapeared_at')