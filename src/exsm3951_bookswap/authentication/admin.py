from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member

# Register your models here.
class MemberAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'address', 'genre_preference', 'is_superuser')


admin.site.register(Member, MemberAdmin)

