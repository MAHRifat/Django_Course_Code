from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="user Name")
    email = forms.EmailField(label="uesr email")