from django.urls import path
# from book.views import home,store_book,show_books,edit_book,delete_book
from . import views

urlpatterns = [
    # class base views
    
    # path('',views.TemplateView.as_view(template_name='home.html')),
    path('',views.HomeView.as_view(),name="home_page"),
    path('show_books/',views.BookListView.as_view(),name="show_books"),
    path('books_details/<int:id>', views.BookDetailView.as_view(), name = 'book_details'),
    path('book_store/', views.BookFormView.as_view(), name="store_book"),
    
    # function base urls
    
    # path('', views.home,name="home_page"),
    # path('store_book/', views.store_book,name="store_book"),
    # path('show_books/', views.show_books,name="show_books"),
    path('edit_book/<int:id>', views.edit_book, name="edit_book"),
    path('delete_book/<int:id>', views.delete_book, name="delete_book"),
]
