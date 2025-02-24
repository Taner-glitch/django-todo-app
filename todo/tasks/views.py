from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    completed_tasks = Task.objects.filter(completed=True)
    pending_tasks = Task.objects.filter(completed=False)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm() 

    
    return render(request, 'tasks/task_list.html', {
        'form': form,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks  
    })

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id) 
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id) 
    task.delete()
    return redirect('task_list')
