from django.shortcuts import render
from .models import Task
from django.views.generic import ListView
# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'main.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()