from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
# start home page design
def home(request):
    task=Task.objects
    tasks=task.all()
    total=task.count()
    complete=task.filter(isCompleted=True).count()
    incomplete=task.filter(isCompleted=False).count()
    context={
        'tasks':tasks,
        'total':total,
        'complete':complete,
        'incomplete':incomplete,
    }
    return render(request,'home.html',context)



# start to create page for data entry
def create(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mission=request.POST.get('mission')
        duration=request.POST.get('duration')
        startDate=request.POST.get('startDate')
        if not all([name,mission,startDate,duration]):
            context={
                'error':"Some field are missing"
            }
            return render(request,'create.html',context)
           
        else:
            Task.objects.create(
                name=name,
                mission=mission,
                startDate=startDate,
                duration=duration,
            )
            
        return redirect('/')
    return render(request,'create.html')

# start to delete data from database
def delete(request,pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    task.save()
    return redirect('/')

# start to mark as completed

def mark(request,pk):
    task=Task.objects.get(pk=pk)
    task.isCompleted=True
    task.save()
   
    return redirect('/')

 
#  start to make as unmark or uncomplete the task
def unmark(request,pk):
    task=Task.objects.get(pk=pk)
    task.isCompleted=False
    task.save()
   
    return redirect('/')


# start to make data editable from database

def edit(request,pk):
    task=Task.objects.get(pk=pk)
    context={
        'task':task
    }
    return render(request,'edit.html',context)


# to update data

def update(request,pk):
        name=request.POST.get('name')
        mission=request.POST.get('mission')
        duration=request.POST.get('duration')
        startDate=request.POST.get('startDate')
        if not all([name,mission,startDate,duration]):
            context={
                'error':"Some field are missing"
            }
            return render(request,'edit.html',context)
           
        else:
            task=Task.objects.get(pk=pk)
            task.name=name
            task.mission=mission
            task.duration=duration
            task.startDate=startDate
            task.save()
            
            
        return redirect('/')
