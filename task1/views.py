from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    ctx = {
        "Name": "Edieson Amistad",
        "ID": "113367",
    }
    return render(request, "pages/about.html", ctx)


