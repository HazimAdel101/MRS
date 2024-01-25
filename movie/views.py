from django.shortcuts import render

# Create your views here.

def movies(request):
    return render(request, "movies.html")


def top_movies(request):
    return render(request, "top-movies.html")


def movie_details(request):
    return render(request, 'movie-details.html')