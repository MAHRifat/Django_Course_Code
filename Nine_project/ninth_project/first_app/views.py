from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

# Cookie

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


# session

def set_session(request):
    data = {
        'name' : 'Rifat',
        'age' : 23,
        'language' : 'Bangla'
    }
    print(request.session.get_session_cookie_age())     # session kotodin active thakbe second e dibe
    print(request.session.get_expiry_date())            # session er expire day show korbe
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    name = request.session.get('name')
    age = request.session.get('age')
    language = request.session.get('language')
    return render(request,'get_session.html', {'name':name, 'age': age, 'language':language})

def delete_session(request):
    # del request.session['name']           # only delete name 
    request.session.flush()         
    request.session.clear_expired()          # delete all session
    return render(request, 'delete_session.html')
