from django.views import generic
from books.models import Book
from django.http import Http404
import datetime


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        date = self.kwargs.get('pub_date')
        if date:
            try:
                formatted_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                book = Book.objects.get(pub_date=formatted_date)
                prev_book = Book.objects.filter(pub_date__lt=formatted_date).order_by('pub_date').last()
                next_book = Book.objects.filter(pub_date__gt=formatted_date).order_by('pub_date').first()

                return {
                    'books': [book],
                    'prev_book': prev_book,
                    'next_book': next_book
                }
            except:
                raise Http404


        return super().get_context_data(**kwargs)

