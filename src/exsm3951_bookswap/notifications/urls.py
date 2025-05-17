from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_view, name='notifications'),
    path('<int:notification_id>/mark-read', views.mark_notification_as_read, name='mark-notification-read'),
]