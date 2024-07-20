from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView
from .forms import TaskForm
# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'main.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()
    
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})