from io import IncrementalNewlineDecoder
from xml.etree.ElementInclude import include
from django.urls import URLPattern, path, include

app_name = 'users'

URLPattern = [
    path('', include('django.contrib.auth.urls')),
]