from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction
from .utils.google_books import get_cover_image, get_books_data
from .forms import BookForm, CustomEditUserForm
from authentication.models import Member
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

    # Replace with actual wishlist logic
    print(f"Add {book.title} to wishlist for {request.user}")

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
    initial_data = request.GET.dict()  # <- use prefilled query params
    form = BookForm(initial=initial_data)

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library')

    return render(request, 'partials/book_form.html', {'form': form})

@login_required
def update_account(request, pk):
    user = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        post_data = request.POST.copy()
        form = CustomEditUserForm(post_data, isinstance=user)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        #finish entering fields here

        messages.success(request, "Profile updated successfully!")
        return redirect('library') #where should we redirect to?
    else:
        form = CustomEditUserForm(isinstance=user)
        context = {
            'form': form,
        }
    return render(request, 'profile/settings.html', context)