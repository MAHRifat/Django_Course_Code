from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_cookie/', views.get_cookie),
    path('del_cookie/', views.delete_cookie),
]
