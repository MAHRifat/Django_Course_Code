from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, './first/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')
        return render(request, './first/about.html', {'name': name,'email': email,'passwoed': password})
    else:
        return render(request, './first/about.html')

def froms(request):
    # print(request.POST)
        return render(request, './first/from.html')