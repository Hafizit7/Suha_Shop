from django import forms
from .models import Contact

class ContactFrom (forms.ModelForm):

    name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Name" }))

    email = forms.EmailField(widget= forms.EmailInput(attrs ={
        'class': 'form-control', 'placeholder':"Your Email" }))

    phone = forms.CharField(max_length=11, widget= forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder':"Your Phone Number" }))

    masegge = forms.CharField(widget= forms.Textarea(attrs={
        'class': 'form-control','placeholder' :"Your Comment" , 'row': 3 }))

    class Meta:
        model = Contact
        fields = '__all__'