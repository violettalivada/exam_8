from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
