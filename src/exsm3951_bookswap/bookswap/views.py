from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction

# Placeholder code, feel free to replace all
@login_required
def library_view(request):
    my_books = BookListing.objects.filter(member_owner=request.user)
    wishlist = WishList.objects.filter(member=request.user)      
    return render(request, "library/library.html", {
        "my_books": my_books,
        "wishlist": wishlist
    })

# Placeholder code, feel free to replace all
@login_required
def browse_books_view(request):
   
    books = [] 

    return render(request, "browse/browse.html", {
        "books": books
    })