from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from .models import todolist

def task(request):
    tasks = todolist.objects.all()  # Get all tasks from the database
    context = {"tasks": tasks}  # Pass the actual tasks queryset to the template
    return render(request, 'task.html', context)

def form(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        todolist.objects.create(Title=title, Description=description)
        return redirect('task')  # This will now work because of the name in urls.py
    return render(request, 'form.html')
