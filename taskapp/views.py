from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from taskapp.forms import TaskForm

from taskapp.models import Task

# Create your views here.
def index(request):
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show_task")
    else:
        form = TaskForm()
        return render(request,'index.html',{'form':form})        
    
    

    
        
            
def show_task(request):
    tasks= Task.objects.all()
    return render(request,'display.html',{'tasks':tasks})    
    
 
    
    
def update_task(request,id):
    context = {}
    task = get_object_or_404(Task, id = id)
    form = TaskForm(request.POST or None, instance = task)
    if form.is_valid():
        form.save()
        return redirect('/show_task')
    else:
        context["form"] = form
        return render(request, "display_update.html", context)
        
                

# def update_status(request,id):
#     if request.method == 'POST':
#         id = request.POST['id']
#         status = request.POST['status']
#         Task.objects.filter(id = id).update(status=status)
#         return redirect("/show_task") 
#     else:
#         task = get_object_or_404(Task, id = id)
#         form = TaskForm(request.POST or None, instance = task)
#         return render(request,"display_update.html",{'form':form})        


def delete_task(request,id):
    obj = Task.objects.get(id=id)
    obj.delete()
    return redirect("/show_task")    

    
            
    
