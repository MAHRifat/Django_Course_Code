from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# function based view

# def home(request):
#     return render(request, 'home.html')

# class base views

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'rahim', 'age' : 21}
        context.update(kwargs)
        return context

# def store_book(request):
#     if request.method == "POST":
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             # use this redirect for when we click the button we will go the show_books url
#             return redirect('show_books')
#     else:
#         book = BookStoreForm()
    
#     return render(request, 'store_book.html', {'form' : book})

# class base form

# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     # success_url = '/show_books/'           # it's work like redirect
#     success_url = reverse_lazy('show_books')  # it's also work like redirect
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         # return super().form_valid(form)
#         return redirect('show_books')



class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm         
    success_url = reverse_lazy('show_books')  # it's also work like redirect


# Show Books

# def show_books(request):
#     book = BookStoreModel.objects.all()
#     print(book)
#     return render(request, 'show_book.html',{'data' : book})

#class base view

class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'data'
    # query korle nicer code gula use korbo
    
    # Ekjon er nam er list caile get_queryset fun use korbo
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(book_author='Rifat')
    
    # kono column er upor order korte cailte eita use korbo
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'data' : BookStoreModel.objects.all().order_by('book_author')} 
    #     return context

    #order korte help korbo
    # ordering= ['id']   # for revarse order use -id

    # override template 
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name='isStaff.html'
        else:
            template_name = self.template_name
        return [template_name]

class BookDetailView(DetailView):
    model = BookStoreModel
    template_name = 'book_delails.html'
    context_object_name = 'i'
    pk_url_kwarg = 'id'


# Edit Book       

# def edit_book(request, id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = BookStoreForm(instance = book)
#     if request.method == "POST":
#         book = BookStoreForm(request.POST,instance = book)
#         if book.is_valid():
#             book.save()
#             return redirect('show_books')
        
#     return render(request, 'store_book.html', {'form' : form})

# edit class view

class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')


# Delete Book

# def delete_book(request, id):
#     book = BookStoreModel.objects.get(pk = id).delete()
#     # book_home = BookStoreModel.objects.all()
#     return redirect("show_books")

# delete class view

class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_books')



    