from django.shortcuts import render

# Create your views here.

def celebrity(request):
    return render(request, "celebrities.html")