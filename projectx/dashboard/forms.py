from django import forms
from django.db import models
from django.forms import fields 
from .models import Product
from django import forms

class ProductDetails(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'