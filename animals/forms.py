from django import forms
from django.forms import ImageField

from animals.models import Animal


class AnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', False)
        super().__init__(*args, **kwargs)
        for i in self.fields:
            print(self.fields[i].error_messages)
            self.fields[i].error_messages = {'required': 'To pole jest wymagane!',
                                             'invalid_choice': 'Wybierz odpowiednią opcję'}

    name = forms.CharField(max_length=100)
    color = forms.CharField(max_length=100)
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
    # photo = ImageField(required=False)

    class Meta:
        model = Animal
        fields = ('name', 'gender', 'breed', 'owner', 'color', 'notes')


