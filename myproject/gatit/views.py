from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Ingredient, Recipe
# Create your views here.

# class IndexView(TemplateView):
#     template_name = 'index.html'

def index(request):
    all_recipes = Recipe.objects.all()
    context = {'all_recipes':all_recipes}

    return render(request,'index.html', context)
