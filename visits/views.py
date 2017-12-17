from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from visits.models import Visit


class VisitListView(ListView):
    template_name = "visits/list.html"
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmark'] = 'visits'
        context['visits'] = Visit.objects.all()
        return context


class VisitDetailsView(DetailView):
    template_name = "visits/details.html"
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmark'] = 'visits'
        context['visit'] = context.
        return context