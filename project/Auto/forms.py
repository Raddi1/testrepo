from django import forms
from django.forms import ModelForm, EmailInput, TextInput
from django.core.exceptions import ValidationError
from django.forms import CharField
from .models import Product, User


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'rate', 'is_new']
        widgets = {
            'rate': forms.NumberInput(attrs={'min': '1', 'max': '5', 'class': 'form-control'})
        }

class RegistrationUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        data:str = self.cleaned_data['email']
        print("EMAIL VALIDATOR")

        if not data.endswith('@gmail.com'):
            raise ValidationError("Доступні лише пошти із доменом @gmail.com")
        
        return data
    

class LoginUserForm(ModelForm):
    email = CharField(widget=EmailInput)

    class Meta:
        model = User
        fields = ['name', 'email']