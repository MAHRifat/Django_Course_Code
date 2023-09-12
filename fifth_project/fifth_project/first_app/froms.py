from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    age = forms.IntegerField(label="Age")
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    Birth_Day = forms.DateField()
    appointment = forms.DateTimeField()
    CHOICES = [('S','Small'), ('M','Medium'), ('L','Large'), ('XL','Extra Large')]
    size = forms.ChoiceField(choices=CHOICES)
    meal = [('P','Pepperoni'), ('M','Mashroom'), ('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal)