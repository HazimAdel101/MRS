from django.shortcuts import render
from .models import Movie 
# Create your views here.

# def movies(request):
#     title = 'movies'
    
#     all_movies = Movie.objects.all()
    
#     return render(request, "movies.html", {'title': title, 'all_movies': all_movies})

def movies(request):
    title = 'movies'
    all_movies = Movie.objects.all()
    print(all_movies)  # Add this line to print the queryset
    return render(request, "movies.html", {'title': title, 'all_movies': all_movies})




def top_movies(request):
    title = 'Top Movies'
    return render(request, "top-movies.html", {'title': title})


def movie_details(request):
    title = 'Details'
    return render(request, 'movie-details.html', {'title': title})