from django.shortcuts import render, redirect
from .models import Task, CompletedTask
from .forms import TaskForm
from django.utils import timezone


# Create your views here.
def task_list(request):
    tasks = Task.objects.filter(is_completed=False).order_by("due_date")
    context = {"tasks": tasks, "name": "İşler"}
    return render(request, "app_1/task_list.html", context)


def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
        else:
            form = TaskForm()
    context = {"form": form, "name": "Görev Ekle"}
    return render(request, "app_1/add_task.html", context)


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    context = {"form": form, "task": task, "name": "Düzenle"}
    return render(request, "app_1/edit_task.html", context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    context = {"task": task, "name": "Sil"}
    return render(request, "app_1/delete_task.html", context)


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.complete_task()
        return redirect("task_list")
    context = {"task": task, "name": "Tamamla"}
    return render(request, "app_1/complete_task.html", context)


def completed_tasks(request):
    completed_tasks = CompletedTask.objects.all().order_by("-completed_at")
    context = {"completed_tasks": completed_tasks, "name": "Tamamlananlar"}
    return render(request, "app_1/completed_tasks.html", context)


def delete_completed_task(request, completed_task_id):
    completed_task = CompletedTask.objects.get(id=completed_task_id)
    if request.method == "POST":
        completed_task.delete()
        print("deleted")
        return redirect("completed_tasks")

    context = {"task": completed_task, "name": "Sil"}
    return render(request, "app_1/delete_completed_task.html", context)
