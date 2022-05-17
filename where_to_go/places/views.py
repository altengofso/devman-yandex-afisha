from django.shortcuts import render

from .models import Place


def index(request):
    data = {
        'type': 'FeatureCollection',
        'features': [],
    }

    for place in Place.objects.all():
        # feature = {
        #     'type': 'Feature',
        #     'geometry': {
        #         'type': 'Point',
        #         'coordinates': [place.longitude, place.latitude],
        #     },
        #     'properties': {
        #         'title': place.title,
        #         'placeId': place.id,
        #         'detailsUrl': {
        #             'title': place.title,
        #             'imgs': [image.image.url for image in place.image_set.all()],
        #             'description_short': place.description_short,
        #             'description_long': place.description_long,
        #             'coordinates': {
        #                 'lng': place.longitude,
        #                 'lat': place.latitude,
        #             },
        #         },
        #     },
        # }

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': '/static/places/moscow_legends.json',
            },
        }

        data['features'].append(feature)

    print(data)

    return render(request, 'index.html', context={'data': data})
