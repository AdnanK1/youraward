from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def home(request):
    context = {}
    return render(request,'home.html',context)

def loginPage(request):
    context = {}
    return render(request,'auth/login.html',context)

def register(request):
    form = CreateUserForm()
    context = {'form':form}
    return render(request,'auth/register.html',context)