
from django.contrib import admin
from django.urls import path
from AppToDo.views import TaskList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskList.as_view(), name='main')
]
