from django.urls import path
from .views import catalog_list, home

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog_list, name='catalog'),
]
