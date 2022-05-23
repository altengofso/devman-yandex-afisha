from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200, unique=True)
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Полное описание')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    order = models.PositiveIntegerField(default=0, db_index=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'
