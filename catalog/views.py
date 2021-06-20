from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from catalog.forms import BrickModelForm, ManualModelForm, SetModelForm
from catalog.models import Brick, Manual, Set


def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Uložení celkového počtu filmů v databázi do proměnné num_films
    number_of_bricks = Brick.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    bricks = Brick.objects.order_by('-type')[:3]
    for brick in bricks:
        print("FILM.IMAGE: ", brick.image)

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'number_of_bricks': number_of_bricks,
        'bricks': bricks
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


# BRICK VIEWS
class BrickListView(ListView):
    model = Brick

    content_object_name = 'brick_list'
    template_name = 'Brick/list.html'
    paginate_by = 16


class BrickDetailView(DetailView):
    model = Brick

    context_object_name = 'brick'
    template_name = 'Brick/detail.html'


class BrickCreateView(CreateView):
    model = Brick

    form_class = BrickModelForm
    template_name = 'catalog/brick_bootstrap_form.html'


class BrickUpdateView(UpdateView):
    model = Brick

    #fields = ['id', 'name', 'color', 'type', 'image', 'sets']
    form_class = BrickModelForm
    template_name = 'catalog/brick_bootstrap_form.html'


class BrickDeleteView(DeleteView):
    model = Brick

    success_url = reverse_lazy('brick_list')


# MANUAL VIEWS
class ManualListView(ListView):
    model = Manual

    content_object_name = 'manual_list'
    template_name = 'Manual/list.html'
    paginate_by = 5


class ManualDetailView(DetailView):
    model = Manual

    context_object_name = 'manual'
    template_name = 'Manual/detail.html'


class ManualCreateView(CreateView):
    model = Manual

    form_class = ManualModelForm
    template_name = 'catalog/manual_bootstrap_form.html'


class ManualUpdateView(UpdateView):
    model = Manual

    form_class = ManualModelForm
    template_name = 'catalog/manual_bootstrap_form.html'


class ManualDeleteView(DeleteView):
    model = Manual

    success_url = reverse_lazy('manual_list')


# SET VIEWS
class SetListView(ListView):
    model = Set

    content_object_name = 'set_list'
    template_name = 'Set/list.html'
    paginate_by = 5


class SetDetailView(DetailView):
    model = Set

    context_object_name = 'set'
    template_name = 'Set/detail.html'


class SetCreateView(CreateView):
    model = Set

    form_class = SetModelForm
    template_name = 'catalog/set_bootstrap_form.html'


class SetUpdateView(UpdateView):
    model = Set

    form_class = SetModelForm
    template_name = 'catalog/set_bootstrap_form.html'


class SetDeleteView(DeleteView):
    model = Set

    success_url = reverse_lazy('set_list')
