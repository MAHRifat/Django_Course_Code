from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.home, name="home_page"),
    path('about/',views.about, name="about_page"),
]
