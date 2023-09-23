from django import forms
from first_app.models import TO_Do_Model

class To_Do_Form(forms.ModelForm):
    class Meta:
        model = TO_Do_Model
        exclude = ['is_completed','id']