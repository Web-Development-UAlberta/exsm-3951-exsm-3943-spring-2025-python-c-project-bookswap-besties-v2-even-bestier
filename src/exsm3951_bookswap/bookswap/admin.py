from django.contrib import admin
from .models import Book, Review, WishList, Shipment, Transaction, BookListing, TransactionDetail, LibraryItem


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'isbn', 'title', 'author', 'genre', 'description', 'pub_date', 'language', 'weight']
    
class BookListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'library_item', 'member_owner', 'price', 'condition', 'is_closed']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member', 'rating', 'review']


class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member']
    
       
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'shipment_date', 'shipment_cost'] 
    
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_type', 'transaction_date', 'initiator_member', 'receiver_member']

class TransactionDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction', 'shipment', 'book_listing', 'from_member', 'to_member', 'cost']
    
class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member']
    
         
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionDetail, TransactionDetailAdmin)
admin.site.register(BookListing, BookListingAdmin)
admin.site.register(LibraryItem, LibraryItemAdmin)
    
