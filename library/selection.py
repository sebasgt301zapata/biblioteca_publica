from .models import Book


class LoanSelection:
    def __init__(self, request):
        self.session = request.session
        selection = self.session.get('selection')

        if not selection:
            selection = self.session['selection'] = {}

        self.selection = selection

    def add_book(self, book):
        book_id = str(book.id)
        if book_id not in self.selection:
            self.selection[book_id] = {}
        self.save()

    def remove_book(self, book):
        book_id = str(book.id)
        if book_id in self.selection:
            del self.selection[book_id]
            self.save()

    def clear(self):
        self.session['selection'] = {}
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        book_ids = self.selection.keys()
        books = Book.objects.filter(id__in=book_ids)

        for book in books:
            yield {
                'book': book
            }

    def __len__(self):
        return len(self.selection)

