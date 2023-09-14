from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = '__all__'
        # fields = ['name','roll']
        exclude =[
            'address']
        
        labels = {
            'name' : 'Student name',
            'roll' : 'Student roll',
            'father_name' : 'Studetn Father name',
            'address' : 'Studetn address'

        }
        
        widgets = {
            'name' : forms.TextInput()
            }
        
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_massages = {
            'name' : "your name is required"
        }