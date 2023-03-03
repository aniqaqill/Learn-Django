from django.shortcuts import render
from django.http import HttpResponse

from .models import Book

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def book_by_id(request, book_id):
    book=Book.objects.get(pk=book_id)
    # return HttpResponse("Book Title: {book.title} Book Published Date: {book.pub_date}".format(book=book))
    return render(request, 'book_details.html', {'book': book})



