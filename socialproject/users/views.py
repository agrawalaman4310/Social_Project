from django.shortcuts import render
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.http import HttpResponse
# Create your views here.

def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data  
            user = authenticate(request,username=data['username'], password=data['password'])
            if user is not None:
                login(request,user)
                return render(request , 'users/login_success.html')
            else:
                return HttpResponse("Invalid Login")   
        
    else:
        form=LoginForm()
    return render(request, 'users/login.html' , {'form':form})

@login_required
def index(request):
    return render(request , 'users/index.html')
