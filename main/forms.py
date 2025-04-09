from .models import *
from django import forms


class NewOpros_answerForm(forms.ModelForm):
    class Meta:
        model = Opros_answer
        fields = ('opros_body', 'body','summary_rating','confidence_level',)
        exclude = ['author']

