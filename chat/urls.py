# chat/urls.py

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserProfileViewSet, ChatModelViewSet, ChatNotificationViewSet

router = SimpleRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'chat-messages', ChatModelViewSet)
router.register(r'chat-notifications', ChatNotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
