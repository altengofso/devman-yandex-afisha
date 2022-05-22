import json
import requests
from django.core.files.base import ContentFile
from ...models import Place, Image


def load_place(path):
    if path.startswith('http'):
        response = requests.get(path)
        response.raise_for_status()
        data = response.json()
    else:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    place, created = Place.objects.get_or_create(
        title=data['title'],
        description_long=data['description_long'],
        description_short=data['description_short'],
        longitude=data['coordinates']['lng'],
        latitude=data['coordinates']['lat'],
    )

    if created:
        for img in data['imgs']:
            response = requests.get(img)
            if not response.ok:
                continue
            content = ContentFile(response.content)
            filename = img.split('/')[-1]
            image = Image.objects.create(place=place)
            image.image.save(filename, content, save=True)
