from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Book, BookListing, Review, WishList, Shipment, Transaction, TransactionDetail, LibraryItem
from .utils.google_books import get_cover_image, get_books_data
from .forms import BookForm, BookListingForm, SwapOfferForm, ReviewForm
from notifications.models import Notification
from django.contrib import messages
from decimal import Decimal 

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
def library_view(request):  # All Listings"  
    search_title = request.GET.get('search_title', '')
    # filtering for book listings of books that contain the title that is being searched for
    # exclude the book listings owned by logged in user
    book_listings = BookListing.objects.filter(is_closed=False).exclude(member_owner=request.user)
    if search_title:
        book_listings = BookListing.objects.filter(library_item__book__title__icontains=search_title)
    return render(request, "library/library.html", {'book_listings': book_listings})


@login_required
def view_my_book_listings(request):
    my_book_listings = BookListing.objects.filter(member_owner=request.user).exclude(is_closed=True)
    return render(request, "book-listings/my-book-listings.html", {
        "my_book_listings": my_book_listings,
    })

@login_required
def browse_books_view(request):
    title = request.GET.get('title')
    author = request.GET.get('author')
    genre = request.GET.get('genre')
    
    books = Book.objects.all()

    if title:
        books = books.filter(title__icontains=title)
    if author:
        books = books.filter(author__icontains=author)
    if genre:
        books = books.filter(genre__iexact=genre)

    my_library_items = LibraryItem.objects.filter(member=request.user).select_related('book')
    my_library_books = [item.book for item in my_library_items]
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
    book_listings = BookListing.objects.filter(library_item__book=book).exclude(is_closed=True)
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
    show_modal = bool(results) or request.GET.get('show_modal') == '1'
    return render(request, 'browse/browse.html', {
        "book_data_list": results,
        "books": Book.objects.all(),
        "show_modal": show_modal,
    })

@login_required
def book_create_from_search(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browse_books')
        
        return render(request, 'partials/book_form.html', {'form': form, 'request': request, 'query': request.GET.get('q', '')})
        
    else:
    
        initial_data = request.GET.dict()  # <- use prefilled query params
        form = BookForm(initial=initial_data)
        
        #make fields readonly
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' bg-gray-100 cursor-not-allowed'

    return render(request, 'partials/book_form.html', {'form': form, 'request': request, 'query': request.GET.get('q', '')})


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
            'price': Decimal("0.01"),
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
        form = BookListingForm(request.POST, instance=book_listing, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_my_book_listings')
    else:
        form = BookListingForm(instance=book_listing, user=request.user)
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

# Buy Transaction 
@login_required
def buy_book(request, book_listing_id):
    book_listing = get_object_or_404(BookListing, pk=book_listing_id)

    if request.method == 'POST':
        # create a pending transaction for the book listing
        transaction = Transaction(
            transaction_type=Transaction.TransactionType.sale,
            transaction_status=Transaction.TransactionStatus.pending,
            initiator_member=request.user,
            receiver_member=book_listing.member_owner,
        )
        transaction.save()

        shipment = Shipment(
            shipment_date=datetime.now().date(),
            shipment_cost=Decimal("10.00"),
            weight=2,
            address="1st AVE EAST Mock Town, Canada"
        )
        shipment.save()
        
        transaction_detail = TransactionDetail(
            transaction=transaction,
            book_listing=book_listing,
            shipment=shipment,
            cost=Decimal(str(book_listing.price)) + Decimal(str(shipment.shipment_cost)),
            from_member=book_listing.member_owner,  # book listing is transfering from 'from_member' to the logged in user
            to_member=request.user,
        )
        transaction_detail.save()
        # notify the owner of the book listing of the buy offer so they can accept / reject it
        notification = Notification(
            member=book_listing.member_owner,
            message=f'You have a buy offer on your listing! <a style="color: blue;" href="/library/transactions/{transaction.id}">View Offer</a>',
            title=f"Buy Offer for {book_listing.library_item.book.title}!"
        )
        notification.save()
        messages.success(request, f"Buy offer sent!")
    
    return redirect('all_listings') # all listings page


@login_required
def transactions_view(request):
    # get all transaction that the user is from ("receiver of transaction") or to ("initiater") in
    transactions = Transaction.objects.filter(Q(initiator_member=request.user) | Q(receiver_member=request.user)).order_by('-id')
    return render(request, "transactions/transactions.html", {'transactions': transactions})


@login_required
def transaction_view(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, "transactions/transaction.html", {'transaction': transaction})

@login_required
def accept_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    # accepting a buy / swap offer
    # go through each transaction detail, and transfer ownership of the book to the to_member
    transaction_details = transaction.transaction_details.all()
    transactions_to_reject = set()
    for detail in transaction_details:
        new_owner = detail.to_member
        # transfer ownership of the library item
        library_item = detail.book_listing.library_item
        library_item.member = new_owner
        library_item.save()
        # mark book listing as closed so it cannot be interacted with again
        book_listing = detail.book_listing
        book_listing.is_closed = True
        book_listing.save()
        
        # notify the 'to_memeber' about the accepted transaction and the new library item in their library
        notification = Notification(
            member=new_owner,
            message=f'Your {transaction.transaction_type} offer was accepted for {library_item.book.title}! <a style="color: blue;" href="/library/my-library/">View your library with the new item</a>',
            title=f"{transaction.transaction_type} Offer accepted :)"
        )
        notification.save()
        
        # collect any other transaction that deals with the book listings invovled in this transaction
        other_transaction_details = TransactionDetail.objects.filter(book_listing=book_listing).exclude(transaction=transaction)
        for detail in other_transaction_details:
            transactions_to_reject.add(detail.transaction)
            

    # mark the transaction as accepted
    transaction.transaction_status = Transaction.TransactionStatus.accepted
    transaction.save()
    
    # other transactions to reject which invovled the same book listing that was accepted in this transaction
    for t in transactions_to_reject:
        t.transaction_status = Transaction.TransactionStatus.rejected
        t.save()
        notification = Notification(
            member=t.initiator_member,
            message=f'Your {t.transaction_type} offer was rejected! <a style="color: blue;" href="/library/transactions/{t.id}">View transaction details</a>',
            title=f"{t.transaction_type} Offer rejected :("
        )
        notification.save()
    
    messages.success(request, f"You accepted the {transaction.transaction_type} transaction!")
    # future enhancement: Add the selling price to the member's balance
    return render(request, "transactions/transaction.html", {'transaction': transaction})

@login_required
def reject_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    
    # Mark transaction as rejected
    transaction.transaction_status = Transaction.TransactionStatus.rejected
    transaction.save()

    # notify the to memeber about the rejected transaction
    notification = Notification(
        member=transaction.initiator_member,
        message=f'Your {transaction.transaction_type} offer was rejected! <a style="color: blue;" href="/library/transactions/{transaction.id}">View transaction details</a>',
        title=f"{transaction.transaction_type} Offer rejected :("
    )
    notification.save()
    messages.success(request, f"You rejected {transaction.transaction_type} transaction!")
    return render(request, "transactions/transaction.html", {'transaction': transaction})


@login_required
def swap_offer_view(request, book_listing_id):
    # the book listing the logged in user is trying to swap for
    book_listing = get_object_or_404(BookListing, pk=book_listing_id)
    
    if request.method == 'POST':
        form = SwapOfferForm(request.POST, user=request.user)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            selected_book_listings = form.cleaned_data['selected_book_listings']
            # Create swap transaction
            transaction = Transaction(
                transaction_type=Transaction.TransactionType.swap,
                transaction_status=Transaction.TransactionStatus.pending,
                initiator_member=request.user,
                receiver_member=book_listing.member_owner,
            )
            transaction.save()

            shipment = Shipment(
                shipment_date=datetime.now().date(),
                shipment_cost=Decimal("10.00"),
                weight=2,
                address="1st AVE EAST Mock Town, Canada"
            )
            shipment.save()
            # create a transaction detail for the book the logged in member wants to own
            transaction_detail = TransactionDetail(
                transaction=transaction,
                book_listing=book_listing,
                shipment=shipment,
                cost=Decimal("0.00"),
                from_member=transaction.receiver_member,
                to_member=request.user,
            )
            transaction_detail.save()
            
            # create a transaction detail for each book listing the logged in user is offering to swap to the receiver
            for listing in selected_book_listings:
                transaction_detail = TransactionDetail(
                    transaction=transaction,
                    book_listing=listing,
                    shipment=shipment,
                    cost=Decimal("0.00"),
                    from_member=request.user,
                    to_member=transaction.receiver_member,
                )
                transaction_detail.save()
            # notify the owner of the book listing of the buy offer so they can accept / reject it
            notification = Notification(
                member=transaction.receiver_member,
                message=f'You have a swap offer on your listing! <a style="color: blue;" href="/library/transactions/{transaction.id}">View Offer</a>',
                title=f"Swap Offer for {book_listing.library_item.book.title}!"
            )
            notification.save()
            messages.success(request, f"Swap offer sent!")
            return redirect('transaction_view', transaction.id)
    else:
        form = SwapOfferForm(user=request.user)
    
    my_book_listings = BookListing.objects.filter(member_owner=request.user)
    my_book_listings_dict = { str(listing.id): listing for listing in my_book_listings }
    return render(request, 'transactions/swap-form.html', {'form': form, 'my_book_listings_dict': my_book_listings_dict, 'book_listing': book_listing})


@login_required
def edit_review(request, book_id):
    # Make sure the logged-in user owns the book
    library_item = get_object_or_404(LibraryItem, book__id=book_id, member=request.user)
    book = library_item.book

    # Try to get an existing review for this book and member, or create a new one
    review, created = Review.objects.get_or_create(book=book, member=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('library')  # Change to your actual library view name
    else:
        form = ReviewForm(instance=review)

    return render(request, 'library/edit_review.html', {
        'form': form,
        'book': book
    })