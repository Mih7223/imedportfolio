from django.shortcuts import render
from .models import Projet


# Create your views here.
def home(request):
    projets = Projet.objects.all()
    return render(request, 'portfolio/home.html', {'projets':projets})
