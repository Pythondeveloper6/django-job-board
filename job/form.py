from django import forms

from .models import Apply




class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name' ,'email','webiste','cv','cover_letter']
