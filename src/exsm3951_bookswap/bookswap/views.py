from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction
from .utils.google_books import get_cover_image

# Placeholder code, feel free to replace all
@login_required
def library_view(request):
    my_books = BookListing.objects.filter(member_owner=request.user)
    wishlist = WishList.objects.filter(member=request.user)      
    return render(request, "library/library.html", {
        "my_books": my_books,
        "wishlist": wishlist
    })

@login_required
def browse_books_view(request):
    books = Book.objects.all()
    for book in books:
        book.image_url = get_cover_image(book.title, book.author)
    return render(request, "browse/browse.html", {"books": books})

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Replace with actual wishlist logic
    print(f"Add {book.title} to wishlist for {request.user}")

    # Redirect back to where they came from
    return redirect(request.META.get('HTTP_REFERER', 'browse_books'))