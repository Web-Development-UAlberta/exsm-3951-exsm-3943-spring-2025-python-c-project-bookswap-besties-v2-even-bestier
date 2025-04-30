from django.contrib import admin
from .models import Book, Review, WishList, Swap, Shipment, SwapDetail


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'isbn', 'title', 'author', 'member']
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member', 'rating', 'review']


class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'member']
    
        
class SwapAdmin(admin.ModelAdmin):
    list_display = ['id'] 
    
       
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'shipment_cost'] 
    
       
class SwapDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'swap' ,'book', 'original_owner', 'new_owner', 'shipment'] 
    
       
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Swap, SwapAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(SwapDetail, SwapDetailAdmin)
    
