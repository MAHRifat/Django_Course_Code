from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home_page"),
    path('about/', views.about, name="about_page"),
    path('from/', views.froms, name="from_page")
]
 