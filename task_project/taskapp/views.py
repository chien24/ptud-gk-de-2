from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Task, Category
from .forms import TaskForm, CategoryForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    categories = Category.objects.filter(created_by=request.user)
    return render(request, 'taskapp/task_list.html', {
        'tasks': tasks,
        'categories': categories
    })

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    return render(request, 'taskapp/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskapp/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            if task.status == 'completed' and not task.finished_at:
                task.finished_at = timezone.now()
                task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskapp/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'taskapp/task_confirm_delete.html', {'task': task})

@login_required
def category_list(request):
    categories = Category.objects.filter(created_by=request.user)
    return render(request, 'taskapp/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'taskapp/category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'taskapp/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('category_list')
    return render(request, 'taskapp/category_confirm_delete.html', {'category': category})