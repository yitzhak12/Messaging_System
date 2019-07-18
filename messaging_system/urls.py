from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('sign_up/', views.add_new_user, name='add_new_user'),
    path('messages', views.get_messages, name='show_messages'),
    path('unread_messages/', views.get_unread_messages, name='show_unread_messages'),
    path('read_message/<int:pk>/', views.read_message, name='show_message'),
    path('write_message/', views.create_new_message, name='write_message'),
    path('delete_message/<int:pk>/', views.delete_message, name='delete_message'),
]