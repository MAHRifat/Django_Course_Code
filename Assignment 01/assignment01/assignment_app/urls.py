from django.urls import path
from . import views

urlpatterns = [
    path('contain/', views.contain)
]
