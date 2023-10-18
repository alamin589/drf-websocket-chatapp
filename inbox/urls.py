# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageList.as_view(), name='message-list'),
    path('messages/<int:receiver_id>/', views.UserChatHistory.as_view(), name='user-chat-history'),
]
