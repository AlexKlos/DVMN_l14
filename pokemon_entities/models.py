from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя Покемона')
    title_en = models.CharField(max_length=200, verbose_name='Имя анг.',
                                null=True,
                                blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Имя яп.',
                                null=True,
                                blank=True)
    image = models.ImageField(upload_to='pokemon_images', 
                              verbose_name='Изображение Покемона', 
                              null=True, 
                              blank=True)
    description = models.TextField(verbose_name='Описание',
                                   null=True,
                                   blank=True)
    previous_evolution = models.ForeignKey('self', 
                                           on_delete=models.SET_NULL, 
                                           verbose_name='Из кого эволюционирует',
                                           related_name='next_evolutions',
                                           null=True,
                                           blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, 
                                on_delete=models.CASCADE, 
                                verbose_name='Покемон',
                                related_name='entities',
                                null=True, 
                                blank=True)
    latitude = models.FloatField(verbose_name='широта')
    longitude = models.FloatField(verbose_name='долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления',
                                       null=True,
                                       blank=True)
    disapeared_at = models.DateTimeField(verbose_name='Время исчезновения',
                                         null=True,
                                         blank=True)
    level = models.PositiveSmallIntegerField(verbose_name='Уровень',
                                             null=True,
                                             blank=True)
    health = models.PositiveSmallIntegerField(verbose_name='Здоровье',
                                              null=True,
                                              blank=True)
    strength = models.PositiveSmallIntegerField(verbose_name='Сила',
                                                null=True,
                                                blank=True)
    defence = models.PositiveSmallIntegerField(verbose_name='Защита',
                                               null=True,
                                               blank=True)
    stamina = models.PositiveSmallIntegerField(verbose_name='Выносливость',
                                               null=True,
                                               blank=True)
