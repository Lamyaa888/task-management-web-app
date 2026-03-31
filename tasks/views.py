from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks_list.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description
        )

        messages.success(request, "Task added successfully!")
        return redirect('task_list')

    return render(request, 'add_task.html')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()

        messages.success(request, "Task updated successfully!")
        return redirect('task_list')

    return render(request, 'edit_task.html', {'task': task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('task_list')

    return render(request, 'delete_task.html', {'task': task})


@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()

    if task.completed:
        messages.success(request, "Task marked as completed!")
    else:
        messages.success(request, "Task marked as not completed!")

    return redirect('task_list')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('task_list')

    return render(request, 'register.html', {'form': form})