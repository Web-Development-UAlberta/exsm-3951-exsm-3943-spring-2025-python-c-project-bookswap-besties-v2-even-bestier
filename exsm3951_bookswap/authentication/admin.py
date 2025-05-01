from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member

# Register your models here.
class MemberAdmin(UserAdmin):
    model = Member

    list_display = ('id', 'email', 'first_name', 'last_name', 'address', 'genre_preference', 'wishlist_books','is_superuser')

    # fields = ['address']


admin.site.register(Member, MemberAdmin)

