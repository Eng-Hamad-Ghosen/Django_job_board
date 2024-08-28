from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile
from .forms import SignupForm , ProfileForm ,UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def signup(request):
    if request.method=='GET':
        form=SignupForm
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            if request.POST['password1']==request.POST['password2']:
                form.save()
                # username=request.POST['username']
                # password=request.POST['password1']
                # print(username)
                # print(password)
                username=form.cleaned_data['username']
                password=form.cleaned_data['password1']
                # print(username)
                # print(password)
                user=authenticate(username=username,password=password)
                login(request,user)
                return redirect(reverse('accounts:profile'),{})
    return render(request,'registration/signup.html',{'form':form})
    
            
def profile(request):
    profile=Profile.objects.get(user=request.user)
    
    return render(request,'account/profile.html',{'profile':profile})       

def profile_edit(request):
    ob_profile=Profile.objects.get(user=request.user)
    ob_user=User.objects.get(username=request.user)
    
    if request.method=='GET':
        # profileform=ProfileForm(instance=ob_profile)
        # userform =UserForm(instance=ob_user)
        
        profileform=ProfileForm(instance=ob_profile)
        userform =UserForm(instance=request.user)
        return render(request,'account/profile_edit.html',{'userform':userform , 'profileform':profileform})
        
    if request.method=='POST':
        profileform=ProfileForm(request.POST , request.FILES , instance=ob_profile)
        userform =UserForm(request.POST,instance=request.user)
        
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
       
        # # form=ProfileForm(request.POST,request.FILES)
        # profile.mobile=request.POST['mobile']
        # print(request.POST)
        # profile.image=request.POST['csrfmiddlewaretoken']
        # profile.save()
        profile=Profile.objects.get(user=request.user)
            
        return redirect(reverse('accounts:profile'))