from django.forms import ModelForm
from libros.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ()
