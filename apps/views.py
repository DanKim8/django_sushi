from django.shortcuts import render
from django.http import HttpResponse

from .models import Appetizer, Sushi, Sashimi, A_La_Carte, Rolls, Vegetarian_Rolls, Special_Rolls, WB_Special_Rolls

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def findDistinctVals(table, column):
    return table.objects.values_list(column, flat = true).distinct()

#List the things on the menu
def getEntities(Entity, EntityName):





#def menu(request):
    context = {
	    "Appetizer": getEntities(Appetizer, "Appetizer"),
		"Sushi": getEntities(Sushi, "Sushi"),
		"Sashimi": getEntities(Sashimi, "Sashimi"),
		"A_La_Carte": getEntities(A_La_Carte, "A_La_Carte"),
		"Rolls": getEntities(Rolls, "Rolls"),
		"Vegetarian_Rolls": getEntities(Vegetarian_Rolls, "Vegetarian_Rolls"),
		"Special_Rolls": getEntities(Special_Rolls, "Special_Rolls"),
		"WB_Special_Rolls": getEntities(WB_Special_Rolls, "WB_Special_Rolls"),
	}
#def home(request):   