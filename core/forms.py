from django.forms import ModelForm
from django import forms
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class JobTypeForm(forms.ModelForm):
    class Meta:
        model = JobType
        fields = '__all__'
