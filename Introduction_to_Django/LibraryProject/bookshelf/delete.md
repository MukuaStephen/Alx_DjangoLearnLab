# Delete the book instance

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

## Output (this command will return a tuple, so we can check it)

book_to_delete
