from django.shortcuts import render  # , redirect

# from django.http import HttpResponse
# from django,utils.text import slugify
from .models import Task


def task_list(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/task/list.html', {'tasks': tasks})
