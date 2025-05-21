from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction, LibraryItem
from .utils.google_books import get_cover_image, get_books_data
from .forms import BookForm, BookListingForm
from authentication.models import Member
from notifications.models import Notification
from django.contrib import messages

@login_required
def my_library_view(request):
    search_title = request.GET.get('search_title', '')
    # filtering for book listings of books that contain the title that is being searched for
    # only include the book listings owned by logged in user
    library_items = []
    if search_title:
        library_items = LibraryItem.objects.filter(book__title__icontains=search_title, member_id=request.user).order_by('book__title')
    else:
        library_items = LibraryItem.objects.filter(member_id=request.user).order_by('book__title')
    return render(request, "library/my_library.html", {'library_items': library_items})

@login_required
def add_to_library(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Add the book as a library item for the user
    new_library_item = LibraryItem(book=book, member=request.user)
    new_library_item.save()

    # Redirect back to where they came from
    return redirect('my_library')

@login_required
def remove_from_my_library(request, listing_id):
    library_item = get_object_or_404(LibraryItem, id=listing_id)
    library_item.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'my_library'))


@login_required
def library_view(request):  #All Listings"  
    search_title = request.GET.get('search_title', '')
    # filtering for book listings of books that contain the title that is being searched for
    # exclude the book listings owned by logged in user
    book_listings = []
    if search_title != '':
        book_listings = BookListing.objects.filter(library_item__book__title__icontains=search_title).exclude(member_owner=request.user)
    return render(request, "library/library.html", {'book_listings': book_listings})


@login_required
def view_my_book_listings(request):
    my_book_listings = BookListing.objects.filter(member_owner=request.user)
    return render(request, "book-listings/my-book-listings.html", {
        "my_book_listings": my_book_listings,
    })

@login_required
def browse_books_view(request):
    books = Book.objects.all()
    my_library_books = Review.objects.filter(member=request.user)
    # Optional inline search support
    query = request.GET.get('q')
    book_data = get_books_data(query) if query else None  

    return render(request, "browse/browse.html", {
        "books": books,
        "book_data": book_data,
        "my_wishlisted_books": request.user.wishlist_books.all(),
        "my_library_books": my_library_books,
    })

@login_required
def view_wishlist(request):
    wishlist_items = WishList.objects.filter(member=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist_items})

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Add the book as a wishlist item for the user
    wishlist_item = WishList(book=book, member=request.user)
    wishlist_item.save()
    
    # Create notifications for all the listing(s) of the book
    book_listings = BookListing.objects.filter(library_item__book=book)
    my_book_listings = request.user.book_listings.all()

    for book_listing in book_listings:
        if book_listing in my_book_listings:
            continue
        notification = Notification(
            title=f'{book_listing.member_owner.full_name} has a listing for the book "{book.title}"!',
            message=f'Follow the link to the book listing <a style="color: blue;" href="/library/book-listings/{book_listing.id}">{book.title}</a>',
            member=request.user,
        )
        notification.save()

    # Redirect back to where they came from
    return redirect(request.META.get('HTTP_REFERER', 'browse_books'))


@login_required
def remove_from_wishlist(request, wishlist_id):
    wishlist_item = get_object_or_404(WishList, id=wishlist_id)
    wishlist_item.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'browse_books'))
    



@login_required
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
            return redirect('browse_books')
        
        return render(request, 'partials/book_form.html', {'form': form})
        
    else:
    
        initial_data = request.GET.dict()  # <- use prefilled query params
        form = BookForm(initial=initial_data)
        
    return render(request, 'partials/book_form.html', {'form': form})


@login_required
def view_book_listing(request, book_listing_id):
    book_listing = get_object_or_404(BookListing, pk=book_listing_id)
    return render(request, 'book-listings/book-listing.html', {'book_listing': book_listing})

# TODO: Create Book listing view (which will trigger notifications creation)
# Create
@login_required
def create_book_listing(request):
    if request.method == 'POST':
        form = BookListingForm(request.POST, user=request.user)
        if form.is_valid():
            new_listing = form.save()
            # Send a notification to users who have this book on their wishlist
            # Step 1: Get all users who have the book in their wishlist
            wishlist_items = WishList.objects.filter(book=new_listing.library_item.book).exclude(member=request.user)
            # Step 2: Create a notification record to each user about that new book listing
            for item in wishlist_items:
                notification = Notification(
                    title=f'{new_listing.member_owner.full_name} has a listing for the book "{new_listing.library_item.book.title}"!',
                    message=f'Follow the link to the book listing <a style="color: blue;" href="/library/book-listings/{new_listing.id}">{new_listing.library_item.book.title}</a>',
                    member=item.member,
                )
                notification.save()
                
            return redirect('view_my_book_listings')
    else:
        intial_data = {
            'member_owner': request.user,
            'price': 0.00,
        }
        form = BookListingForm(initial=intial_data, user=request.user)

        # form.fields['library_item'].choices = LibraryItem.objects.filter(member=request.user).all()
        return render(request, 'book-listings/book-listing-form.html', {'form': form, 'title': 'Create Book Listing', 'submit_button_text': 'Create'})


# Update
@login_required
def edit_book_listing(request, book_listing_id):
    book_listing = get_object_or_404(BookListing, pk=book_listing_id)
    # make sure only the owner can edit their book listing
    if book_listing.member_owner != request.user:
        return redirect('view_my_book_listings')

    if request.method == 'POST':
        form = BookListingForm(request.POST, instance=book_listing)
        if form.is_valid():
            form.save()
            return redirect('view_my_book_listings')
    else:
        form = BookListingForm(instance=book_listing)
        # Make sure the user cannot update the book of an existing listing
        # form.fields['book'].disabled = True
        return render(request, 'book-listings/book-listing-form.html', {'form': form, 'title': 'Update Book Listing', 'submit_button_text': 'Save'})


# Delete
@login_required
def delete_book_listing(request, book_listing_id):
    book_listing = get_object_or_404(BookListing, pk=book_listing_id)
    if request.method == 'POST':
        book_listing.delete()
        return redirect('view_my_book_listings')
    return render(request, 'book-listings/book-listing.html', {'book_listing': book_listing})


