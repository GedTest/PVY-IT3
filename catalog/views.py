from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Brick, Manual, Set


def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Uložení celkového počtu filmů v databázi do proměnné num_films
    number_of_bricks = Brick.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    films = Brick.objects.order_by('-type')[:3]
    for film in films:
        print("FILM.IMAGE: ", film.image)

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'number_of_bricks': number_of_bricks,
        'films': films
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)





#def index(request):
#    return render(request, 'index.html')


class BrickListView(ListView):
    model = Brick

    content_object_name = 'brick_list'
    template_name = 'Brick/list.html'
    paginate_by = 16


class BrickDetailView(DetailView):
    model = Brick

    context_object_name = 'brick'
    template_name = 'Brick/detail.html'
