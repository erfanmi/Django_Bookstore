from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'price']
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books_list')


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'content']
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('books_list')


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')
