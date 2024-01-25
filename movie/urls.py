from django.urls import path
from . import views


urlpatterns = [
    path('', views.movies, name='movie'),
    path('top-movies', views.top_movies, name='top_movies')
]