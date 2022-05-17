from django.urls import path
from .views import index, place_detail


urlpatterns = [
    path('', index),
    path('places/<int:place_id>/', place_detail, name='place_detail'),
]
