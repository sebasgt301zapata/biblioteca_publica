from django.contrib import admin
from .models import Category, Book, Reader, Loan, LoanItem

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Loan)
admin.site.register(LoanItem)
