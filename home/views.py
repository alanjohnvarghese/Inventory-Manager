# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as lgn
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
 
from .models import Tool, ToolLog
import datetime

# Create your views here.


def start(request):
    template='home/home.html'
    return render(request,template,{})

def signup(request):
    template='home/signup.html'
    return render(request,template,{})

def signupHandler(request):
    uname=request.POST['name']
    pwd=request.POST['password']
    u=User.objects.create_user(username=uname , password=pwd)
    u.save()
    return loginHandler(request)


def login(request):
    template='home/login.html'
    return render(request,template,{})


def loginHandler(request):
    usern=request.POST['name']
    pwd=request.POST['password']
    user= authenticate(username=usern, password=pwd)
    if user is not None:
        lgn(request,user)
        return redirect('/loginpage/')
    else:
        return render(request, 'home/login.html',{})

@csrf_exempt 
def toolput(request):
    try:
        if request.method == "GET":
            usern=request.GET['uid']
            pwd=request.GET['pwd']
            tlid=request.GET['tlid']
        else:
            usern=request.POST['uid']
            pwd=request.POST['pwd']
            tlid=request.POST['tlid']
        p_user= authenticate(username=usern, password=pwd)
        if p_user is not None:
            #if p_user.is_staff==True:
                t=Tool.objects.get(tool_id=tlid)
                t.current=None
                t.current_time = None
                t.save()
                tl = ToolLog(tool = t , user = p_user,date = datetime.datetime.now() ,status = 1)
                tl.save()
                return HttpResponse("admin!")
            
        else:
            return HttpResponse("no user")    
    except KeyError:
        return HttpResponse("keyerror")

@csrf_exempt
def toolget(request):
    try:
        if request.method == "GET":
            usern=request.GET['uid']
            pwd=request.GET['pwd']
            tlid=request.GET['tlid']
        else:
            usern=request.POST['uid']
            pwd=request.POST['pwd']
            tlid=request.POST['tlid']
        p_user= authenticate(username=usern, password=pwd)
        if p_user is not None:
            #if p_user.is_staff==True:
                t=Tool.objects.get(tool_id=tlid)
                t.current=p_user
                t.current_time = datetime.datetime.now()
                t.save()
                tl = ToolLog(tool = t , user = p_user,date = datetime.datetime.now() ,status = 0)
                tl.save()
                return HttpResponse("admin!")
            
        else:
            return HttpResponse("no user")    
    except KeyError:
        return HttpResponse("keyerror")

def loginpage(request):
    template='home/loginpage.html'
    loggedin=None
    if request.user.is_authenticated():
        loggedin=request.user.username
    tu=Tool.objects.filter(current=request.user)
    t=Tool.objects.all()
    to=[]
    for i in t:
        if i not in tu and i.current:
            to.append(i)
    ta=[]
    for i in t:
        if not i.current:
            ta.append(i)
    p={'u':loggedin, 'tu':tu, 'to':to,'ta':ta}
    return render(request,template,p)

