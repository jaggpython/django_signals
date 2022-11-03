from django.shortcuts import render, redirect
from django.contrib import auth
from email import message
from django.contrib import messages
from datetime import datetime





def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.info(request, f'Welcome to {user}')
            return redirect('/admin')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return render(request,'login.html', {'current_time':current_time})
