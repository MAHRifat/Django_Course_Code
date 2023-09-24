from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fi','Sci-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    book_author = models.CharField(max_length=20)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_published = models.DateTimeField(auto_now_add=True) # django ekdom first data
    last_published = models.DateTimeField(auto_now=True) # erpor joto update korbo sei date dethabe
    
    def __str__(self) -> str:
        return f"{self.book_name}  - {self.book_author}"