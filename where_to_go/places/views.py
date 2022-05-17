from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def index(request):
    data = {
        'type': 'FeatureCollection',
        'features': [],
    }

    for place in Place.objects.all():

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_detail', args=[place.id]),
            },
        }

        data['features'].append(feature)

    return render(request, 'index.html', context={'data': data})


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    data = {
        'title': place.title,
        'imgs': [image.image.url for image in place.image_set.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        },
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 2})
