from django import forms
from django.forms import ModelForm

from owners.models import Owner


class OwnerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', False)
        super().__init__(*args, **kwargs)
        for i in self.fields:
            print(self.fields[i].error_messages)
            self.fields[i].error_messages = {
                'required': 'To pole jest wymagane!',
                'invalid_choice': 'Wybierz odpowiednią opcję'}

    full_name = forms.CharField(max_length=100)
    phone_number = forms.RegexField(regex=r'^[0-9]{9,11}$')
    # phone_number = forms.RegexField(
    # regex=r'/^(?:\(?\+?48)?(?:[-\.\(\)\s]*(\d)){9}\)?$/') # ^[0-9]{9,11}$
    location = forms.CharField(max_length=100)

    class Meta:
        model = Owner
        fields = ['full_name', 'phone_number', 'email', 'location',
                  'recommended_by']
