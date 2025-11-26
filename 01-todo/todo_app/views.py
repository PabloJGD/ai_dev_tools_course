from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from django.urls import reverse

def todo_list(request):
    todos = TodoItem.objects.all().order_by('due_date')
    return render(request, 'home.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        if due_date == '':
            due_date = None
        
        TodoItem.objects.create(
            title=title,
            description=description,
            due_date=due_date
        )
        return redirect('todo_list')
    return render(request, 'todo_form.html') # We might need a separate form template or reuse home

def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        if due_date == '':
            due_date = None
        todo.due_date = due_date
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_confirm_delete.html', {'todo': todo})

def todo_complete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todo_list')
