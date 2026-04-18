from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    return render(request, 'tasks/register.html', {'form': form})


@login_required
def task_list(request):
    filter_type = request.GET.get('filter', 'all')

    tasks = Task.objects.filter(user=request.user)

    if filter_type == 'active':
        tasks = tasks.filter(completed=False)
    elif filter_type == 'done':
        tasks = tasks.filter(completed=True)

    return render(request, 'tasks/index.html', {'tasks': tasks})


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('/')


@login_required
def api_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    data = list(tasks.values('id', 'title', 'completed'))
    return JsonResponse(data, safe=False)

from django.shortcuts import redirect, get_object_or_404
from .models import Task

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('/')