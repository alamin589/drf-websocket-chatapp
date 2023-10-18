# views.py
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# You may also create an API view for retrieving a user's chat history
class UserChatHistory(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        receiver_id = self.kwargs.get('receiver_id')
        return Message.objects.filter(sender=user, receiver_id=receiver_id) | Message.objects.filter(sender_id=receiver_id, receiver=user)
