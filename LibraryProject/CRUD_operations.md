# CRUD Operations for Book Model

## Create Operation

To create a new book, we used the following command:

```python
from bookshelf.models import Book

# Creating a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output
book
