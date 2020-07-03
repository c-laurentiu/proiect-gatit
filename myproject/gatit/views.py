from django.views.generic import TemplateView, ListView
from .models import Ingredient, Recipe
from django.db.models import Q
from functools import reduce
from operator import and_, or_
# Create your views here.

# class IndexView(TemplateView):
#     template_name = 'index.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search_results.html'

    def get_queryset(self):
        args = Q()
        input_query = self.request.GET.get('q')
        query_list = input_query.split(' ')
        print(query_list)
        queries = [Q(ingredients__ingredient__icontains = value) for value in query_list]
        query = reduce(and_, (Q(ingredients__ingredient__icontains = value) for value in query_list))
        # for item in queries:
        #     query &= item
        print(query)
        object_list = Recipe.objects.filter(query).distinct()

        test = Recipe.objects.get(pk=1).ingredients.all()
        print(test)




        # for each_arg in query_list:
        #     if args != Q():
        #         args = Q(ingredients__ingredient__icontains=each_arg)
        #     else:
        #         args = Q(ingredients__ingredient__icontains=each_arg)
        #     print(each_arg)
        #     print(args)
        #
        # object_list = Recipe.objects.filter(*(args,)).distinct()
        print(type(query))
        # print(test_query)
        print(object_list)
        return object_list
