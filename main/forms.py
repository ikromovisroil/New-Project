from .models import *
from django import forms


class NewAnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ('title', 'area', 'eksports','name','imports','body','volume','category',)
        exclude = ['author']
    
