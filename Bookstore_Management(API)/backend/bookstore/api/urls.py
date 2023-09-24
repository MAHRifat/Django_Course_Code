from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookListview,basename="book")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('', include(router.urls)),
    path('books/', views.BookListview.as_view()),  #get, post request handle korbe
    path('books/<int:pk>/', views.BookListDeleteUpdate.as_view()),
]