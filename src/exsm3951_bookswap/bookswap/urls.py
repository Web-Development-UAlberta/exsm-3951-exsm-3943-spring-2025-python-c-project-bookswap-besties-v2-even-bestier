from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_view, name='library'),
    path('browse/', views.browse_books_view, name='browse_books'),
    path('browse/search/', views.book_search_view, name='book_search'),
    path('books/create/', views.book_create_from_search, name='book_create_from_search'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('my-book-listings/', views.view_my_book_listings, name='view_my_book_listings'),
    path('book-listings/create', views.create_book_listing, name='create_book_listing'),
    path('book-listings/<int:book_listing_id>/', views.view_book_listing, name='view_book_listing'),
    path('book-listings/<int:book_listing_id>/edit', views.edit_book_listing, name='edit_book_listing'),
    path('book-listings/<int:book_listing_id>/delete', views.delete_book_listing, name='delete_book_listing'),
    path('my-library/', views.my_library_view, name='my_library'),
    
]