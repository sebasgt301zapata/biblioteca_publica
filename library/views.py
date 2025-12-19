from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib import messages
from .models import Book, Category
from .forms import CategoryForm, BookForm
from .selection import LoanSelection
from django.shortcuts import redirect, render
from .models import Reader, Loan, LoanItem, Book

# --------------------
# CATEGORÍAS
# --------------------

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'library/category_form.html'
    success_url = reverse_lazy('book_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'library/category_confirm_delete.html'
    success_url = reverse_lazy('book_list')

# --------------------
# LIBROS
# --------------------

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


# --------------------
# CATÁLOGO
# --------------------

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

# --------------------
# CARRITO / SELECCIÓN
# --------------------

def add_to_selection(request, book_id):
    selection = LoanSelection(request)
    book = get_object_or_404(Book, id=book_id)
    selection.add_book(book)
    messages.success(request, 'Libro agregado a la selección')
    return redirect('selection_detail')


def remove_from_selection(request, book_id):
    selection = LoanSelection(request)
    book = get_object_or_404(Book, id=book_id)
    selection.remove_book(book)
    return redirect('selection_detail')



def selection_detail(request):
    selection = LoanSelection(request)
    return render(request, 'library/selection_detail.html', {
        'selection': selection
    })


def confirm_loan(request):
    selection = LoanSelection(request)

    if len(selection) == 0:
        return redirect('book_list')

    reader = Reader.objects.first()
    loan = Loan.objects.create(reader=reader)

    for item in selection:
        LoanItem.objects.create(
            loan=loan,
            book=item['book']
        )

    selection.clear()

    return render(request, 'library/loan_confirmed.html', {
        'loan': loan
    })
