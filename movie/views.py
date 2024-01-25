from django.shortcuts import render

# Create your views here.

def movies(request):
    title = 'movies'
    return render(request, "movies.html", {'title': title})


def top_movies(request):
    title = 'Top Movies'
    return render(request, "top-movies.html", {'title': title})


def movie_details(request):
    title = 'Details'
    return render(request, 'movie-details.html', {'title': title})