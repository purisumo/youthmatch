from django.forms import ModelForm
from django import forms
from registration.models import User
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        labels = '__all__'

class JobTypeForm(forms.ModelForm):
    class Meta:
        model = JobType
        fields = '__all__'

class ProfileUpdateForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=JobType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile', 'address', 'email', 'education', 'country', 'region', 'exp', 'skills']