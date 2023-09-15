from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.

def home(request):
    return render(request, 'base.html')

def store_book(request):
    if request.method == "POST":
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            # use this redirect for when we click the button we will go the show_books url
            return redirect('show_books')
    else:
        book = BookStoreForm()
    
    return render(request, 'store_book.html', {'form' : book})

def show_books(request):
    book = BookStoreModel.objects.all()
    print(book)
    return render(request, 'show_book.html',{'data' : book})

def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method == "POST":
        book = BookStoreForm(request.POST,instance = book)
        if book.is_valid():
            book.save()
            return redirect('show_books')
        
    return render(request, 'store_book.html', {'form' : form})

def delete_book(request, id):
    book = BookStoreModel.objects.get(pk = id).delete()
    # book_home = BookStoreModel.objects.all()
    return redirect("show_books")
    