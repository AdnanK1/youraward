from django.shortcuts import render,redirect
from .forms import CreateUserForm,SubmitProject
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required(login_url='login')
def home(request):
    context = {}
    return render(request,'home.html',context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist ')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {'page':page}
    return render(request,'auth/login.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            subject = 'Welcome to YourAward'
            message = f'Hello {username} we welcome you to YourAward Application'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject,message,from_email,recipient_list, fail_silently=False)
            user = form.save()
            login(request,user,backend = 'django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    context = {'form':form}
    return render(request,'auth/register.html',context)

@login_required(login_url='login')
def submission(request):
    form = SubmitProject()
    if request.method == 'POST':
        form = SubmitProject(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'submission.html',context)

def user(request):
    context = {}
    return render(request,'user.html',context)

def profile(request):
    context = {}
    return render(request,'profile.html',context)