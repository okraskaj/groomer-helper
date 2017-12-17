from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView

from animals.models import Animal


class AnimalListView(ListView):
    template_name = "breeds-list.html"
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['bookmark'] = 'animals'
        context['breeds'] = Animal.objects.all()
        return context


class AnimalDetailsView(DetailView):
    template_name = "breed-details.html"
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmark'] = 'animals'
        context['breeds'] = Animal.objects.all()
        return context


class AnimalView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['context'] = context
            return context

