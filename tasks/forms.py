from django import forms
from django.db.models.base import Model

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title',  'description')
        
