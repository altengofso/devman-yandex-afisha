import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from ...models import Place, Image


class Command(BaseCommand):
    help = 'Loading new place from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        url = options['file']
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
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
