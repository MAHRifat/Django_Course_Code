from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def home(request):
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
    return render(request, 'home.html',{'form': form})