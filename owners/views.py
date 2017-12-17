from django.shortcuts import render

# TODO: ostatnia wizyta
# TODO: koniecznie w liscie filtry- też łączone i jak wyżej
# TODO: zaznaczanie na liście <haczyki>
# TODO: przycisk w prawym górnym rogu do smsów

# Create your views here.
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from owners.models import Owner


class OwnerListView(ListView):
    template_name = "owners/list.html"
    model = Owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = Owner.objects.all()
        return context


class OwnerDetailsView(DetailView):
    template_name = "details.html"
    model = Owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Owner: " + str(context['owner'])
        context['breeds'] = Owner.objects.all()
        return context