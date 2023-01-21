from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter your username.."
        }) 
        )
    email = forms.EmailField(
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your email.."
            }) 
            )
    password1 = forms.CharField(
            widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your password.."
            }) 
            )
    password2 = forms.CharField(label='Confirm your password',max_length=30,
            widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "placeholder":"Confirme password.."
            }) 
            )   
            
    class Meta:
        model=User
        fields =['first_name', 'last_name', 'username', 'email', 'password1','password2']