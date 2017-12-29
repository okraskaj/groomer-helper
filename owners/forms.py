from django.forms import ModelForm

from owners.models import Owner


class ArticleForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['full_name', 'phone_number', 'email', 'location']
