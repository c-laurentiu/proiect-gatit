from django.views.generic import TemplateView, ListView
from .models import Ingredient, Recipe
from gatit.forms import EntryCreationForm
from django.db.models import Q
from functools import reduce
from operator import and_, or_
# Create your views here.

# class IndexView(TemplateView):
#     template_name = 'index.html'

class HomePageView(ListView):
    template_name = 'home.html'
    model = Ingredient
    # if 'search' in request.GET


class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.getlist('q')
        if query != None:
            object_list = Recipe.objects.all()
            for item in query:
            # if len(query) > 1:
                object_list = object_list.filter(
                        Q(ingredients__ingredient_name__icontains = item)
                        ).distinct()
                # criteria = reduce(and_, (Q(ingredients__ingredient_name__icontains = item) for item in query))
                # object_list = Recipe.objects.filter(criteria).distinct()
                # print(criteria)
            # else:
            #     object_list = Recipe.objects.filter(
            #         Q(ingredients__ingredient_name__icontains = query)
            #         ).distinct()
            for i in object_list: #algoritm ca la codul vechi
                break



        print(query)
        print(object_list)

        return object_list
