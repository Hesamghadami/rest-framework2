from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser, Profile



class CustomUserCreation(UserCreationForm):



    class Meta:
        model = CustomeUser
        fields = [ 'email','username', 'password1', 'password2']




class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    email = forms.EmailField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )


class EditProfile(forms.ModelForm):



    class Meta:
        model = Profile
        fields = [ 'user','first_name', 'last_name', 'image', 'phone', 'address']