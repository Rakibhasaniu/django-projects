from django.shortcuts import render
from . import forms
# Create your views here.

def add_task(request):
    task_form = forms.TakForm()
    return render(request, 'add_task.html', {'data': task_form})