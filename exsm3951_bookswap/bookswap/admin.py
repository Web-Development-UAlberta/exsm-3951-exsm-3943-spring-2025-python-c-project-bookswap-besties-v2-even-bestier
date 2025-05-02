from django.contrib import admin
from .models import Book, Review, WishList, Swap, Shipment, Transaction


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'member','isbn', 'title', 'author', 'genre', 'description', 'pub_date', 'condition', 'language', 'price', 'weight']
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member', 'rating', 'review']


class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member']
    
        
class SwapAdmin(admin.ModelAdmin):
    list_display = ['id'] 
    
       
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'shipper', 'recipient', 'shipment_cost'] 
    
    
class TransactionAdmin(admin.ModelAdmin):
    swap = models.ForeignKey(Swap, on_delete=models.CASCADE, null=True)  # null when transaction_type is Sale
    list_display = ['transaction_type', 'transaction_date', 'shipment', 'book', 'from_member', 'to_member', 'cost', 'swap']
    
         
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Swap, SwapAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Transaction, TransactionAdmin)
    
