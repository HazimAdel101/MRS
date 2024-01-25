from django.shortcuts import render

# Create your views here.

def celebrity(request):
    title = 'Celebrity'
    return render(request, "celebrities.html", {'title': title})