from django import forms
from .models import Ingredient, Recipe

class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['ingredients'].queryset = Ingredient.objects.none()
