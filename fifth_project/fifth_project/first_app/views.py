from django.shortcuts import render
from . froms import contactForm

# Create your views here.

def home(request):
    return render(request, './first/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        return render(request, './first/about.html', {'name': name,'email': email,'select': select})
    else:
        return render(request, './first/about.html')

def froms(request):
    # print(request.POST)
        return render(request, './first/from.html')
    
def Django_Form(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, './first/django_form.html', {'form' : form})