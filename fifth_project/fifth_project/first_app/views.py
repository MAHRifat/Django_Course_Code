from django.shortcuts import render

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