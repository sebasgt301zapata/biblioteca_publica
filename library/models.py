from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nombre de la categoría"
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Título"
    )
    author = models.CharField(
        max_length=100,
        verbose_name="Autor"
    )
    year = models.IntegerField(
        verbose_name="Año de publicación"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Categoría"
    )

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def active_loans_count(self):
        return self.loans.filter(returned=False).count()

    def last_loan(self):
        return self.loans.order_by('-created_at').first()


class Loan(models.Model):
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE,
        related_name='loans'
    )
    created_at = models.DateTimeField(default=timezone.now)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Préstamo #{self.id} - {self.reader.name}"

    def total_books(self):
        return self.items.count()

    def is_active(self):
        return not self.returned

    def mark_returned(self):
        self.returned = True
        self.save()


class LoanItem(models.Model):
    loan = models.ForeignKey(
        Loan,
        on_delete=models.CASCADE,
        related_name='items'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.book.title}"