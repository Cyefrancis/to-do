from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import TaskForm
from django.urls import reverse_lazy
# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'main.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()
    
class createTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('main')