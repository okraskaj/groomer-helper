from django import forms
from django.forms import ModelForm

from visits.models import Visit


class VisitForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', False)
        super().__init__(*args, **kwargs)
        for i in self.fields:
            print(self.fields[i].error_messages)
            self.fields[i].error_messages = {
                'required': 'To pole jest wymagane!',
                'invalid_choice': 'Wybierz odpowiednią opcję'}

    start = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'datepicker',
        'data-provide': 'datepicker-inline',
    }))
    stop = forms.DateTimeField()

    class Meta:
        model = Visit
        fields = ['animal', 'start', 'stop', 'service', 'happened',
                  'money_taken', 'notes']
