from email import message
from multiprocessing import context
from turtle import title
from django import db
from django.shortcuts import redirect, render
from home.models import task,contactuser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    if request.method == "POST":
        tasktitle=request.POST['tasktitle']
        taskdescripion=request.POST['taskdescription']
        user=request.user
        detail=task(Task = tasktitle , Task_Description = taskdescripion,user=user )
        messages.success(request, request.user.username+", Your Task has been Added")
        detail.save()
    return render(request, 'index.html' )
def contact(request):
    context={'success':False , 'msg1':'Hey' , 'msg2':"Have querry? Contact Us"}
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        address=request.POST['address']
        description=request.POST['description']
        contactuserdetail=contactuser(Name=name , Address = address , Description=description , Email=email)
        contactuserdetail.save()
        context={'success':False , 'msg1':'Thank You' , 'msg2':name+", we will let you soon."}
    return render(request, 'contact.html' ,context)
def about(request):
    return render(request, 'index.html')
def task1(request):
    try:
        alltask=task.objects.filter(user=request.user)
        print(alltask)
        context = {'tasks':alltask}
        return render(request, 'tasklist.html' ,context)
    except:
        alltask=None
        context = {'tasks':alltask}
        return render(request, 'tasklist.html' ,context)
def base(request):
    return render (request, 'base.html')
def handelsignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        pass1=request.POST['pass1']
        user=User.objects.create_user(username,email,pass1)
        user.save()
        messages.success(request, "Your account has been created.")
        return redirect("/")
def handellogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully loged in")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/")
def handlelogout(request):
    username=request.user
    logout(request)
    messages.success(request, "You are successfully loged out")
    return redirect("/")
def update(request,sno):
    if request.method=="POST":
        title = request.POST['tasktitle']
        description = request.POST['taskdescription']
        task.objects.filter(sno=sno).update(Task=title,Task_Description=description)
        messages.success(request, request.user.username+", Your Task has been updatd")
        return redirect("/task")
        
    taskupdated=task.objects.filter(sno=sno).first()
    context={"taskupdated":taskupdated,"updateboard":True}
    print(taskupdated.Task_Description)
    return render(request, "update.html",context)
def deletetask(request,sno):
    if request.method=="GET":
        record=task.objects.get(sno=sno)
        print(record)
        print(record.delete())
        messages.success(request, request.user.username+", Your Task has been Deleted")
    return redirect("/task")