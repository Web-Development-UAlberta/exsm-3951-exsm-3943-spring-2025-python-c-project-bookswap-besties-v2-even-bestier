from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_view, name='notifications'),
    path('<int:notification_id>/mark-read', views.mark_notification_as_read, name='mark-notification-read'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete-notification'),
]