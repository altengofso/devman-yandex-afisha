from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=1000)
    description_long = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    order = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.order} {self.place.title}'

    class Meta:
        ordering = ['place', 'order']