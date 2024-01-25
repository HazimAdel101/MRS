from django.shortcuts import render

# Create your views here.
# why do get error page not found where i am trying to get the template from the main app created from django?


#  pass a variable value ?
def home(request):
    title = 'Home'
    return render(request, "index.html", {"title": title})