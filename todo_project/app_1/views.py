from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "task_list.html", context)


def task(request, task_id):
    taskObj = Task.objects.get(id=task_id)
    context = {"task": taskObj}
    return render(request, "task.html", context)


def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    context = {"form": form}
    return render(request, "add_task.html", context)


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)
    print(task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    context = {"form": form}
    return render(request, "edit_task.html", context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    print(task)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    context = {"task": task}
    return render(request, "delete_task.html", context)  # redirect("delete_task")
