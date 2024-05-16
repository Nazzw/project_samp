from django import forms
from django.forms import ModelForm
from .models import pets
class petsForm(ModelForm):
    class Meta:
        model = pets
        fields = "__all__"
        