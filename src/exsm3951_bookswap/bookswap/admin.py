from django.contrib import admin
from .models import Book, Review, WishList, Swap, Shipment, Transaction, BookListing


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'isbn', 'title', 'author', 'genre', 'description', 'pub_date', 'language', 'weight']
    
class BookListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member_owner', 'price', 'condition']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member', 'rating', 'review']


class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member']
    
        
class SwapAdmin(admin.ModelAdmin):
    list_display = ['id'] 
    
       
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'shipment_date', 'shipment_cost'] 
    
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_type', 'transaction_date', 'shipment', 'book_listing', 'from_member', 'to_member', 'cost', 'swap']
    
         
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Swap, SwapAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(BookListing, BookListingAdmin)
    
