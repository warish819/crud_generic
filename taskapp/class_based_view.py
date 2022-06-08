from django.http import request
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Task

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'index.html'
    # success_url = 'show-task'

class ShowTask(ListView):
    model = Task
    fields = '__all__'
    template_name = 'display.html'
    context_object_name = 'tasks'

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'display_update.html'
    # success_url = '/show-task'  

class DeleteTask(DeleteView):
    model = Task
    template_name = 'deletion/delete.html'
    # success_url = '/show-task'
   
