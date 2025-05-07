from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_view, name='library'), 
    path('browse/', views.browse_books_view, name='browse_books'),
]