from typing import Any
from django import forms
from django.core import validators


# widgets == fiend to html input
class contactForm(forms.Form):
    name = forms.CharField(label="Name", help_text="Total length must be within 70 characters", required=False, disabled=False, widget= forms.Textarea(attrs={'id' : 'text_area', 'placeholder' : 'Enter your name'}))
    # file = forms.FileField()
    # image = forms.ImageField()
    email = forms.EmailField(label="Email")
    age = forms.CharField(widget=forms.NumberInput)
    BirthDay = forms.DateField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'), ('M','Medium'), ('L','Large'), ('XL','Extra Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    meal = [('P','Pepperoni'), ('M','Mashroom'), ('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)
    
# user define validators
def len_check(value):
    if len(value) < 10 :
        raise forms.ValidationError("Enter a value at least 10 chars")
    
    
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message="Enter a name with at least 10 characters")])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField( validators=[validators.MinValueValidator(18,message="Please enter age more than 17"), validators.MaxValueValidator(35,message="Please enter age less then 36")])
    
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'],message="File must be pdf or jpg")])
    
    # text use user define validators
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your eamil must contain .com")
    #     return valemail
    
    # Shortcuts of this
    
    # def clean(self) -> dict[str, Any]:
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your eamil must contain .com")