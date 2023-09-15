from django.contrib import admin
from book.models import BookStoreModel
# Register your models here.

# admin.site.register(BookStoreModel)

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'book_author','category','first_published','last_published')

admin.site.register(BookStoreModel, BookStoreModelAdmin)