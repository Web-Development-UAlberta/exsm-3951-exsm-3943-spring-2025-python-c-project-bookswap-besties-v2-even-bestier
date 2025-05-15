from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction
from .utils.google_books import get_cover_image, get_books_data
from .forms import BookForm
from authentication.models import Member
from notifications.models import Notification
from django.contrib import messages


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

    # Optional inline search support
    query = request.GET.get('q')
    book_data = get_books_data(query) if query else None

    return render(request, "browse/browse.html", {
        "books": books,
        "book_data": book_data
    })

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Add the book as a wishlist item for the user
    wishlist_item = WishList(book=book, member=request.user)
    wishlist_item.save()
    
    # Create notifications for all the listing(s) of the book
    book_listings = BookListing.objects.filter(book=book)
    for book_listing in book_listings:
        notification = Notification(
            title=f'{book_listing.member_owner.full_name} has a listing for the book "{book.title}"!',
            message=f'Follow the link to the book listing <a style="color: blue;" href="/book-listings/{book_listing.id}">{book.title}</a>',
            member=request.user,
        )
        notification.save()
        


    # Redirect back to where they came from
    return redirect(request.META.get('HTTP_REFERER', 'browse_books'))


def book_search_view(request):
    query = request.GET.get('q', '')
    results = get_books_data(query) if query else []
    return render(request, 'browse/browse.html', {
        "book_data_list": results,
        "books": Book.objects.all()
    })

@login_required
def book_create_from_search(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library')


    initial_data = request.GET.dict()  # <- use prefilled query params
    form = BookForm(initial=initial_data)
    return render(request, 'partials/book_form.html', {'form': form})




# TODO: Create Book listing view (which will trigger notifications creation)