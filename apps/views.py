from django.shortcuts import render
from django.http import HttpResponse

from .models import Appetizer, Sushi, Sashimi, A_La_Carte, Rolls, Vegetarian_Rolls, Special_Rolls, WB_Special_Rolls

# Create your views here.

def index(request):
    return render(request, "main/index.html")
