from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_session, name='home'),
    path('get_cookie/', views.get_cookie),
    path('del_cookie/', views.delete_cookie),
    path('get_session/', views.get_session),
    path('del_session/', views.delete_session),
]
