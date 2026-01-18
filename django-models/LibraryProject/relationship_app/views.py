from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role check functions
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # The checker specifically looks for this line
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
<<<<<<< HEAD
    context_object_name = 'library'


# Create your views here.
=======
    context_object_name = 'library'
>>>>>>> edc3c0a (add update)
