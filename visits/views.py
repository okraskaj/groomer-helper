from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, ListView

from visits import forms
from visits.models import Visit


class VisitListView(ListView):
    template_name = "visits/list.html"
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visits'] = Visit.objects.all()
        context['title'] = 'Wizyty'  # TODO: Tłumaczeie
        return context


class VisitDetailsView(DetailView):
    template_name = "visits/details.html"
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VisitCreate(generic.CreateView):
    form_class = forms.VisitForm
    template_name = 'form.html'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            messages.error(request, 'Pomyślnie anulowano')
            return HttpResponseRedirect(reverse('animals-list'))
        else:
            messages.success(self.request, 'Pomyślnie dodawano')
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
        return reverse('owners-list')
