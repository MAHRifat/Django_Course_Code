from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def course(request):
    return HttpResponse('''
                        
                        <h1> This is course page</h1>
                        <a href = '/first_app/about/'> About </a>
                        <a href = '/first_app/contact/'> Contact </a><br>
                        <a href = '/second_app/feedback/'> Feedback </a><br>
                        ''')

def feedback(request):
    return HttpResponse('''
                        
                        <h1> This is course page</h1>
                        <a href = '/first_app/about/'> About </a>
                        <a href = '/first_app/contact/'> Contact </a><br>
                        <a href = '/second_app/course/'> course </a><br>
                        ''')