from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq_view, name='help_faq'),
]