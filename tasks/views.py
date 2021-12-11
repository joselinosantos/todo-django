from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import TaskForm
import datetime

from .models import Task

@login_required
def tasklist(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)
    else: 
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 10)

        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    if request.method == 'POST':
         form = TaskForm(request.POST)
         if form.is_valid():
             task = form.save(commit=False)
             task.done = 'doing'
             task.user = request.user
             task.save()
             return redirect('/')
    else:  
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')
    return render(request, 'tasks/edittask.html', {'form':form, 'task':task})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada')
    return redirect('/')

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if (task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'
    task.save()
    return redirect('/')

@login_required
def dashboard(request):
    tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=30), user=request.user).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    return render(request, 'tasks/dashboard.html', {'tasksRecently': tasksDoneRecently, 'tasksDone': tasksDone, 'tasksDoing':tasksDoing})
