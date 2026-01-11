from django.contrib import admin

from .models import Book

# Step 1 & 2: Define a custom admin class and register the model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a filter sidebar for the publication year
    list_filter = ('publication_year',)
    
    # Enable a search bar that searches through title and author
    search_fields = ('title', 'author')

# Register the model with the customized settings
admin.site.register(Book, BookAdmin)
# Register your models here.
