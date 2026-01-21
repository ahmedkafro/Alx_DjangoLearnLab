from django.urls import path
from .views import admin_view, librarian_view, member_view

#from django.urls import path
from .views import list_books, LibraryDetailView

#from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import add_book, edit_book, delete_book
#from django.urls import path
#from .views import admin_view, librarian_view, member_view

urlpatterns = [
    # ... existing urls ...
   path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

urlpatterns = [
    # Built-in views for login and logout
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Custom registration view
    path('register/', views.register, name='register'),
    
    # Keep your previous URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
##urlpatterns = [
    # ... existing urls ...
  #  path('admin/', admin_view, name='admin_view'),
  #  path('librarian/', librarian_view, name='librarian_view'),
   # path('member/', member_view, name='member_view'),]
