from django import forms
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