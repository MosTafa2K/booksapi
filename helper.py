def search_book(books, book_id: int):
    """Search for a book by its ID in a sorted list of books using binary search."""
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2
        guess_book = books[mid]

        if guess_book["id"] == book_id:
            return mid
        elif guess_book["id"] < book_id:
            low = mid + 1
        else:
            high = mid - 1
    return None
