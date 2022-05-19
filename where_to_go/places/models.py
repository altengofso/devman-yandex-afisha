from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.CharField(max_length=1000)
    description_long = HTMLField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    order = models.PositiveIntegerField(default=0, db_index=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order} {self.place.title}'

    class Meta:
        ordering = ['order']
