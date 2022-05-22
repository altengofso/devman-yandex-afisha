import os
from django.core.management.base import BaseCommand
from . import load_place


class Command(BaseCommand):
    help = 'Loading new places from all JSON files from folder'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        path = options['path']
        files = os.listdir(path)
        for file in files:
            if file.endswith('.json'):
                load_place(path + '/' + file)
