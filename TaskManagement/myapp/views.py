from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    var = Task.objects.all()
    return render(request,'home.html',{'k':var})
def add1(request):
    if request.method=='POST':
        a = request.POST['name']
        b = request.POST['title']
        c = request.POST['desc']
        d = request.POST['status']
        e = request.POST['deadline']
        Task.objects.create(name=a,title=b,desc=c,status=d,deadline=e)
        return redirect('home')
    return render(request,'add1.html')
def update(request,id):
    var=Task.objects.get(id=id)
    if request.method=='POST':
        var.name = request.POST['name']
        var.title = request.POST['title']
        var.desc = request.POST['desc']
        var.status = request.POST['status']
        var.deadline = request.POST['deadline']
        var.save()
        return redirect('home')
    return render(request,'update.html',{'k':var})
def delete(request,id):
    var=Task.objects.get(id=id)
    TaskRestore.objects.create(name=var.name,title=var.title,desc=var.desc,status=var.status,deadline=var.deadline)
    var.delete()
    return redirect('home')
def delete_all(request):
    var=Task.objects.all()
    var1=TaskRestore.objects.bulk_create(var)
    var1.save()
    var.delete()
    return redirect('home')
def history(request):
    var = TaskRestore.objects.all()
    return render(request, 'history.html', {'k': var})
def restore(request,id):
    a = TaskRestore.objects.get(id=id)
    Task.objects.create(name=a.name,title=a.title,desc=a.desc,status=a.status,deadline=a.deadline)
    a.delete()
    return redirect('home')
def restore_all(request):
    var = TaskRestore.objects.all()
    for i in var:
        Task.objects.create(name=i.name,title=i.title,desc=i.desc,status=i.status,deadline=i.deadline)
    var.delete()
    return redirect('e')
def delete_restore(request,id):
    var = TaskRestore.objects.get(id=id)
    var.delete()
    return redirect('e')
def delete_history(request):
    TaskRestore.objects.all().delete()
    return redirect('e')