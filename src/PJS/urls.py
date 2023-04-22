from django.contrib import admin
from django.urls import path
from cities.views import weather_view
from pages.views import (home_view, contact_view, about_me_view, graphs_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about_me/', about_me_view, name='about_me'),
    path('contact/', contact_view, name='contact'),
    path('graphs/', graphs_view, name='graphs'),
    path('weather/', weather_view, name='weather'),
]
