from django import forms

from breeds.models import Breed


class BreedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', False)
        super().__init__(*args, **kwargs)
        for i in self.fields:
            print(self.fields[i].error_messages)
            self.fields[i].error_messages = {'required': 'To pole jest wymagane!',
                                             'invalid_choice': 'Wybierz odpowiednią opcję'}

    name = forms.CharField(max_length=100)
    species = forms.ChoiceField(choices=Breed.SPECIES_CHOICES, initial='pies')
    size = forms.ChoiceField(choices=Breed.SIZE_CHOICES, initial='medium')
    hair_type = forms.ChoiceField(choices=Breed.HAIR_TYPE_CHOICES, initial='normalna')
    grooming_notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
    weight = forms.IntegerField(required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = Breed
        fields = ('name', 'species', 'size', 'hair_type', 'grooming_notes', 'weight', 'photo')
