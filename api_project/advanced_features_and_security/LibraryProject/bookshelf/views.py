from django.shortcuts import render
#from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
# Create your views here.
#from django.shortcuts import render
f#rom django.contrib.auth.decorators import permission_required
#from .models import Book

#from django.shortcuts import render
#from .models import Book
from .forms import BookForm

from .forms import ExampleForm


def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})

def form_example(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, "bookshelf/form_example.html", {"form": form})
from django.http import HttpResponse


def csp_example_view(request):
    response = HttpResponse("CSP Enabled")
    response["Content-Security-Policy"] = "default-src 'self'"
    return response
def safe_search(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_view", raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/view_books.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"],
            author=request.POST["author"]
        )
    return render(request, "bookshelf/create_book.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.save()
    return render(request, "bookshelf/edit_book.html", {"book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request, "bookshelf/delete_book.html")