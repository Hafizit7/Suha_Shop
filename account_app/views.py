from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

def register(request):
    if request.method =='POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form =RegistrationForm()
    return render(request, 'account_app/register.html',{'form':form})

