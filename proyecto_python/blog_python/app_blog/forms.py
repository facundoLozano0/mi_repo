from dataclasses import fields
from django import  forms
from .models import Blogs

class blogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields='__all__'