from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, './first/index.html', context= {'author': 'Phitron', 'age': 19, 'marks': 33, 'courses': [
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