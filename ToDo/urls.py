
from django.contrib import admin
from django.urls import path, include
from AppToDo.views import TaskList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('AppToDo.urls')),
    path('', TaskList.as_view(), name='main')
]
