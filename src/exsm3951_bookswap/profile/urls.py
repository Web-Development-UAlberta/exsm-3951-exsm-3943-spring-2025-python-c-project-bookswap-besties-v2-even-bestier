from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.profile_settings_view, name='profile_settings'),
]