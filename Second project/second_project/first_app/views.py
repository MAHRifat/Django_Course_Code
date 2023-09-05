from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        
                        <h1> This is contact page</h1>
                        <a href = '/first_app/about/'> About </a>
                        <a href = '/second_app/course/'> Course </a><br>
                        <a href = '/second_app/feedback/'> Feedback </a><br>
                        ''')

def about(request):
    return HttpResponse('''
                        
                        <h1> This is about page</h1>
                        <a href = '/first_app/contact/'> Contact </a><br>
                        <a href = '/second_app/course/'> Course </a><br>
                        <a href = '/second_app/feedback/'> Feedback </a><br>
                        
                        
                        ''')
