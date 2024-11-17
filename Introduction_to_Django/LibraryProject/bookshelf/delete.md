# Delete Operation for Book

To delete a book from the database, use the following command:

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")  # Retrieve the book instance
book.delete()  # Delete the book instance
