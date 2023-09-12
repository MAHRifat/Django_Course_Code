from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home_page"),
    path('about/', views.about, name="about_page"),
    path('from/', views.froms, name="from_page"),
    path('django_from/', views.Django_Form, name="django_form_page"),
    path('student_data/', views.studentData, name="django_student_form"),
    path('sign_in/', views.passwordvalid, name="sign_in"),
    
]
 