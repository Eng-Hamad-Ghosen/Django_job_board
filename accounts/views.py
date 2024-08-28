from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from .forms import SignupForm
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
    
            
def profile(reauest):
    pass            