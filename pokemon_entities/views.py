import folium
import json
import os
import datetime

from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from pokemon_entities.models import PokemonEntity, Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def get_image_path(pokemon: Pokemon) -> str:
    image_path = os.path.join(settings.MEDIA_ROOT, pokemon.image.name) if pokemon.image else DEFAULT_IMAGE_URL
    return image_path


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    current_time = datetime.datetime.now()

    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url if pokemon.image else '',
            'title_ru': pokemon.title
        })

        pokemon_entities = PokemonEntity.objects.filter(
            pokemon=pokemon,
            appeared_at__lte=current_time,
            disappeared_at__gte=current_time
        )
        for entity in pokemon_entities:
            image_path = get_image_path(pokemon)
            add_pokemon(
                folium_map,
                entity.latitude,
                entity.longitude,
                image_path
            )

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    current_time = datetime.datetime.now()
    pokemon_entities = PokemonEntity.objects.filter(
        pokemon=requested_pokemon,
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in pokemon_entities:
        image_path = get_image_path(requested_pokemon)
        add_pokemon(
            folium_map,
            entity.latitude,
            entity.longitude,
            image_path
        )

    previous_evolution = None
    next_evolution = None
    if requested_pokemon.previous_evolution:
        previous_evolution = {
            'pokemon_id': requested_pokemon.previous_evolution.id,
            'title_ru': requested_pokemon.previous_evolution.title,
            'img_url': requested_pokemon.previous_evolution.image.url if requested_pokemon.previous_evolution.image else ''
        }
    
    next_pokemon = requested_pokemon.next_evolutions.first()
    if next_pokemon:
        next_evolution = {
            'pokemon_id': next_pokemon.id,
            'title_ru': next_pokemon.title,
            'img_url': next_pokemon.image.url if next_pokemon.image else ''
        }
    

    pokemon_data = {
        'pokemon_id': requested_pokemon.id,
        'title_ru': requested_pokemon.title,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'img_url': requested_pokemon.image.url if requested_pokemon.image else '',
        'description': requested_pokemon.description,
        'next_evolution': next_evolution,
        'previous_evolution': previous_evolution
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_data
    })
