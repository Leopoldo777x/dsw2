from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm, EditTaskForm
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


def task_list_completed(request):
    tasks = Task.objects.filter(completed=True)

    return render(request, 'tasks/task/list_completed.html', {'tasks': tasks})


def edit_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-detail')
    else:
        form = EditTaskForm(instance=task)
    return render(request, 'tasks/task/edit.html', dict(task=task, form=form))


def delete_task(request, task_slug: str):
    Task.objects.get(slug=task_slug).delete()
    return redirect('tasks:task-list')


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():  # Crea objeto AddTaskform
            task = form.save(commit=False)
            task.slug = slugify(task.name)  # slugifea el titulo
            task.save()  # Guarda en baase de datos
            return redirect('tasks:task-list')  # TE lleva a task/tasks/list
    else:
        form = AddTaskForm()
    return render(request, 'tasks/task/add.html', dict(form=form))


def toggle_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:task-list')
