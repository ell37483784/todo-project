from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task


def task_list(request):
    filter_type = request.GET.get('filter', 'all')

    tasks = Task.objects.all()

    if filter_type == 'active':
        tasks = tasks.filter(completed=False)
    elif filter_type == 'done':
        tasks = tasks.filter(completed=True)

    # добавление задачи
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')

    return render(request, 'tasks/index.html', {'tasks': tasks})


def delete_task(request, id):
    task = Task.objects.filter(id=id).first()
    if task:
        task.delete()
    return redirect('/')


def complete_task(request, id):
    task = Task.objects.filter(id=id).first()
    if task:
        task.completed = True
        task.save()
    return redirect('/')


def api_tasks(request):
    tasks = Task.objects.all()
    data = list(tasks.values('id', 'title', 'completed'))
    return JsonResponse(data, safe=False)