from django.shortcuts import render,redirect
from . models import Task
from . forms import todoforms

# Create your views here.



def task_view(request):
    obj=Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj1=Task(name=name,priority=priority,date=date)
        obj1.save()
    return render(request,'taskview.html',{'obj':obj})
def delete (request, delete_id):
    task=Task.objects.get(id=delete_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update (request,update_id):
    task=Task.objects.get(id=update_id)
    form=todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})


