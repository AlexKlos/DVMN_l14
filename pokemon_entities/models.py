from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя Покемона')
    image = models.ImageField(upload_to='pokemon_images', verbose_name='Изображение Покемона', null=True, blank=True)

    def __str__(self):
        return self.title
    

class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='lat')
    longitude = models.FloatField(verbose_name='lon')