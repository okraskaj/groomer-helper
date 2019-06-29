# TODO: ostatnia wizyta
# TODO: koniecznie w liscie filtry- też łączone i jak wyżej
# TODO: zaznaczanie na liście <haczyki>
# TODO: przycisk w prawym górnym rogu do smsów

# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, ListView

from owners import forms
from owners.models import Owner


class OwnerListView(ListView):
    template_name = "owners/list.html"
    model = Owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = Owner.objects.all()
        context['title'] = 'Właściciele'  # TODO: Tłumaczeie
        return context


class OwnerDetailsView(DetailView):
    template_name = "owners/details.html"
    model = Owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Owner: " + str(context['owner'])
        context['breeds'] = Owner.objects.all()
        return context


class OwnerCreate(generic.CreateView):
    form_class = forms.OwnerForm
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
