from django import forms
from .models import Book, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nombre de la categoría'
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'category']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'year': 'Año de publicación',
            'category': 'Categoría'
        }

