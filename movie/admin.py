from django.contrib import admin
from .models import Genre, Movie

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ( "title","director","release_year","rating")

admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)




# list_display = ( "title","director","release_year","rating")