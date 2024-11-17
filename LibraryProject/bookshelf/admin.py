from django.contrib import admin
from .models import Book

# Customizing the Book model's display in the admin interface
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for title and author
    search_fields = ('title', 'author')
    
    # Add filter options based on publication year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)

