from django.contrib import admin

from .models import Appetizer, Sushi, Sashimi, A_La_Carte, Rolls, Vegetarian_Rolls, Special_Rolls, WB_Special_Rolls

# Register your models here.

admin.site.register(Appetizer)
admin.site.register(Sushi)
admin.site.register(Sashimi)
admin.site.register(A_La_Carte)
admin.site.register(Rolls)
admin.site.register(Vegetarian_Rolls)
admin.site.register(Special_Rolls)
admin.site.register(WB_Special_Rolls)
