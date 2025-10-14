from django.http import HttpResponse
from django.shortcuts import render  # , redirect
from django.utils.text import slugify

from .forms import EditPostForm
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


def edit_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := EditPostForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
    else:
        form = EditPostForm(instance=task)
    return render(request, 'tasks/task/edit.html', dict(task=task, form=form))


def delete_task(request, task_slug: str):
    Task.objects.get(slug=task_slug).delete()
    return task_list(request)


def add_task(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():  # Crea objeto Addpostform
            post = form.save(commit=False)
            post.slug = slugify(post.title)  # slugifea el titulo
            post.save()  # Guarda en baase de datos
            return redirect('posts:post-list')  # TE lleva a posts/list
    else:
        form = AddPostForm()
    return render(request, 'posts/post/add.html', dict(form=form))
