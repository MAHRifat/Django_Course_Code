from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, This is a Home page for this website")