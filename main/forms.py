from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sections","price", "description"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none w-full'}),
            'sections': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none w-full'}),
            'price': forms.NumberInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none w-full'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none w-full'}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_sections(self):
        sections = self.cleaned_data["sections"]
        return strip_tags(sections)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)