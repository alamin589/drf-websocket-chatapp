# chat/urls.py

from django.urls import path
from .views import SendMessageView

urlpatterns = [
    path('send-message/<str:room_name>/', SendMessageView.as_view(), name='send-message'),
    # Other URL patterns if you have more
]
