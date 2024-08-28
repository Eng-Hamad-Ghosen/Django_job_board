from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    """Form definition for Signup."""

    class Meta:
        """Meta definition for Signupform."""

        model = User
        fields = ('username','email','password1','password2')
        
class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ['city','mobile','image']

class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ['username','first_name','last_name','email']
