from django.http import HttpResponse
from django.shortcuts import render  # , redirect

# from django,utils.text import slugify
from .models import Task


def task_list(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/task/list.html', {'tasks': tasks})


def task_detail(request, task_slug: str):
    try:
        task = Task.objects.get(slug=task_slug)
    except Task.DoesNotExist:
        return HttpResponse(f'La tarea "{task_slug}" no existe')
    return render(request, 'tasks/task/detail.html', {'task': task})


def task_list_pending(request):
    tasks = Task.objects.filter(completed=False)

    return render(request, 'tasks/task/list_pending.html', {'tasks': tasks})
