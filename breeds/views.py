from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, ListView

from breeds import forms
from breeds.models import Breed


class BreedListView(ListView):
    template_name = "breeds/list.html"
    model = Breed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breeds'] = Breed.objects.all()
        context['title'] = 'Rasy'  # TODO: Tłumaczeie
        return context


class BreedDetailsView(DetailView):
    template_name = "breeds/details.html"
    model = Breed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breeds'] = Breed.objects.all()
        return context


class BreedCreate(generic.CreateView):
    form_class = forms.BreedForm
    template_name = 'form.html'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            messages.error(request, 'Pomyślnie anulowano dodawanie rasy')
            return HttpResponseRedirect(reverse('animals-list'))
        else:
            messages.success(self.request, 'Pomyślnie dodawano rasę')
            return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('breeds-list')
