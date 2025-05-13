from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_view, name='library'), 
    path('browse/', views.browse_books_view, name='browse_books'),
    path('wishlist/add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('browse/search/', views.book_search_view, name='book_search'),
    path('books/create/', views.book_create_from_search, name='book_create_from_search'),
]