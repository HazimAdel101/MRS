from django.shortcuts import render

# Create your views here.
# why do get error page not found where i am trying to get the template from the main app created from django?
def home(request):
    return render(request, "index.html")