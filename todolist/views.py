from django.shortcuts import render, redirect
from .models import todolist

def task(request):
    tasks = todolist.objects.all()  # Get all tasks from the database
    context = {"tasks": tasks}  # Pass the tasks to the template
    return render(request, 'task.html', context)

def form(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        todolist.objects.create(Title=title, Description=description)
        return redirect('task')  # Redirect back to the task list
    return render(request, 'form.html')

def update(request, pk):
    task = todolist.objects.get(pk=pk)
    task.status = not task.status  # Mark the task as completed
    task.save()
    return redirect('task')  # Redirect back to the task list after updating
