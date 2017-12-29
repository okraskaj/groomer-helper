# Create your views here.
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from breeds.models import Breed


class BreedListView(ListView):
    template_name = "breeds/list.html"
    model = Breed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breeds'] = Breed.objects.all()
        return context


class BreedDetailsView(DetailView):
    template_name = "breeds/details.html"
    model = Breed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breeds'] = Breed.objects.all()
        return context
