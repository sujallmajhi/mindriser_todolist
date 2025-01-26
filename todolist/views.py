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

def edit(request, pk):
    task = todolist.objects.filter(pk=pk).first()  # Retrieve task

    if not task:
        return redirect('task')  # If the task doesn't exist, go back to task list

    if request.method == "POST":
        task.Title = request.POST.get('Title', task.Title)  # Get the new title
        task.Description = request.POST.get('Description', task.Description)  # Get the new description
        task.save()  # Save the task with updated data
        return redirect('task')  # Redirect to the task list

    return render(request, 'edit.html', {'task': task})

def delete_task(request, pk):
    # Retrieve the task to delete by its pk
    task = todolist.objects.get(pk=pk)

    # Delete the task
    task.delete()

    # Redirect to the task list after deleting
    return redirect('task')
