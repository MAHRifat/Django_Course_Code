from django.shortcuts import render
from . froms import contactForm
from . froms import StudentData
from . froms import PasswordValidationProject

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

# way 1:

    # form = contactForm(request.POST, request.FILES)
    # if form.is_valid():
    #     file = form.cleaned_data['file']
    #     with open('./first_app/upload/' + file.name , 'wb+') as destination:
    #         for chunk in file.chunks():
    #             destination.write(chunk)
    #     print(form.cleaned_data)
    # return render(request, './first/django_form.html', {'form' : form})

# way 2:
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name , 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render(request, './first/django_form.html', {'form' : form})
    else:
            form = contactForm()
    return render(request, './first/django_form.html', {'form' : form})
            
def studentData(request):
    if request.method == "POST":
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'./first/student_data.html', {'form' : form})
    else:
            form = StudentData()
    return render(request, './first/student_data.html', {'form' : form})


def passwordvalid(request):
    if request.method == "POST":
        form = PasswordValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'./first/password.html', {'form' : form})
    else:
            form = PasswordValidationProject()
    return render(request, './first/password.html', {'form' : form})