from django import forms

from .models import Company, Events

class CompanyCreateForm(forms.ModelForm):
        
    class Meta:
        model = Company
        fields = ('name', 'category', 'logo', 'country', 'province',
            'district', 'city', 'town', 'date_established',
            'official_website','description')
        