from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'Rifat')
    # response.set_cookie('name', 'Hasan', max_age=10)  # override hoye jabe  and the max_age use for set the time of cookie hold is cookies
    response.set_cookie('name','Hasan', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html',{'name': name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response