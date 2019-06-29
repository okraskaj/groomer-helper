from django import forms
from django.forms import ModelForm

from visits.models import Visit


class VisitForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', False)
        super().__init__(*args, **kwargs)
        for i in self.fields:
            print(self.fields[i].error_messages)
            self.fields[i].error_messages = {'required': 'To pole jest wymagane!',
                                             'invalid_choice': 'Wybierz odpowiednią opcję'}

    start = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'datepicker',
        'data-provide': 'datepicker-inline',
    }))
    stop = forms.DateTimeField()

    # email = forms.EmailField()
    # full_name = forms.CharField(max_length=100)
    # phone_number = forms.RegexField(regex=r'^[0-9]{9,11}$')
    # # phone_number = forms.RegexField(regex=r'/^(?:\(?\+?48)?(?:[-\.\(\)\s]*(\d)){9}\)?$/') # ^[0-9]{9,11}$
    # location = forms.CharField(max_length=100)

    class Meta:
        model = Visit
        fields = ['animal', 'start', 'stop', 'service', 'happened', 'money_taken', 'notes']
