from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя Покемона')
    image = models.ImageField(upload_to='pokemon_images', 
                              verbose_name='Изображение Покемона', 
                              null=True, 
                              blank=True)

    def __str__(self):
        return self.title
    

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, 
                                on_delete=models.CASCADE, 
                                verbose_name='Покемон', 
                                null=True, 
                                blank=True)
    latitude = models.FloatField(verbose_name='lat')
    longitude = models.FloatField(verbose_name='lon')
    appeared_at = models.DateTimeField(verbose_name='Время появления',
                                       null=True,
                                       blank=True)
    disapeared_at = models.DateTimeField(verbose_name='Время исчезновения',
                                         null=True,
                                         blank=True)