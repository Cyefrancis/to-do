from django.urls import path
from .views import TaskList, createTask 

urlpatterns = [
    path('main', TaskList.as_view(), name='main'),
    path('create_task/', createTask.as_view(), name='create_task')
]
