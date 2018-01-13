from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, ListView, TemplateView

from animals import forms
from animals.models import Animal


class AnimalListView(ListView):
    template_name = "animals/list.html"
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals'] = Animal.objects.all()
        context['title'] = 'Zwierzęta' #TODO: Tłumaczeie
        return context


class AnimalDetailsView(DetailView):
    template_name = "animals/details.html"
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals'] = Animal.objects.all()
        return context


class AnimalView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['context'] = context
            return context


class AnimalCreate(generic.CreateView):
    form_class = forms.AnimalForm
    template_name = 'form.html'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            messages.error(request, 'Pomyślnie anulowano dodawanie zwierzęcia')
            return HttpResponseRedirect(reverse('animals-list'))
        else:
            messages.success(self.request, 'Pomyślnie dodawano zwierzę')
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
        return reverse('animals-list')