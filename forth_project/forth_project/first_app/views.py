from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, './first/home.html', context= {'name': 'Phitron', 'age': 19, 'marks': 33, 'courses': [
        {
            'id': 1,
            'course': 'C++',
            'teacher': 'Rahim'
        },
        {
            'id': 2,
            'course': 'Java',
            'teacher': 'kahim'
        },
        {
            'id': 3,
            'course': 'Python',
            'teacher': 'Fahim'
        }
    ] })
    
def about(request):
    return render(request, './first/about.html', {'author' : 'glan Mex'})