from django.forms import forms
from .models import Task

class TaskForm(forms.ModeForm):
    class Meta:
        model = Task
        fields = ['title', 'content']