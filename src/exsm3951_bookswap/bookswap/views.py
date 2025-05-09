from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Placeholder code, feel free to replace all
@login_required
def library_view(request):
   
    my_books = []  
    wishlist = []      
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