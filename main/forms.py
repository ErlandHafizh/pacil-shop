from django.forms import ModelForm
from main.models import Product
from django import forms

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