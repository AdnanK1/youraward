from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm,SubmitProject,BioForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile,Project
from .serializer import ProfileSerializer,ProjectSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q)
    )

    profiles =  Profile.objects.all()
    context = {'projects':projects,'profiles':profiles}
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
    form = BioForm()
    if request.method == 'POST':
        form = BioForm(request.POST,request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect('profile') 
    context = {'form':form}
    return render(request,'user.html',context)

@login_required(login_url='login')
def profile(request,pk):
  
    project = Project.objects.get(id=pk)
    profile = Profile.objects.get(id=pk)

    context = {'project':project, 'profile':profile}
    return render(request,'profile.html',context)

class ProjectList(APIView):
    def get(self,request,format=None):
        all_project = Project.objects.all()
        serializer = ProjectSerializer(all_project, many=True)
        return Response(serializer.data)

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profile = Profile.objects.all()
        serializer = ProfileSerializer(all_profile,many=True)
        return Response(serializer.data)

def likeProject(request,pk):
    post = get_object_or_404(Project,id=request.POST.get('like_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('home',args=[str(pk)]))

def logoutUser(request):
    logout(request)
    return redirect('login')