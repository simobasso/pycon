from django.conf import settings


def site_config(request):
    return {
        'GOOGLE_MAPS_KEY': settings.GOOGLE_MAPS_KEY,
    }
