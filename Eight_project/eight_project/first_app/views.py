from django.shortcuts import render,redirect
from .forms import RegisterForm,user_chagne_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                # messages.warning(request, 'warnign')
                # messages.info(request, 'info')
                # messages.error(request, 'errors')
                form.save()
        else:
            form = RegisterForm()
        return render(request, 'signup.html',{'form': form})
    else:
        return redirect('profile')


def User_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)   #check kortechi user database e ache ki na
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{'user' : request.user})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)  # password update korbe
                return redirect('profile')    
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './passchange.html', {'form': form})
    else:
        return redirect('signup')



def pass_change_without_old_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)  # password update korbe
                return redirect('profile')    
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, './passchange.html', {'form': form})
    else:
        return redirect('signup')
    

def ChangeUserData(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = user_chagne_data(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                # messages.warning(request, 'warnign')
                # messages.info(request, 'info')
                # messages.error(request, 'errors')
                form.save()
        else:
            form = user_chagne_data(instance = request.user)
        return render(request, 'changeuserdata.html',{'form': form})
    else:
        return redirect('signup')