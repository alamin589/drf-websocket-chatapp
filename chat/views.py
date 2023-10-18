# # chat_app/views.py

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from chat.serializers import ChatMessageSerializer

# class SendMessageView(APIView):
#     serializer_class = ChatMessageSerializer

#     def post(self, request, room_name):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             channel_layer = get_channel_layer()
#             async_to_sync(channel_layer.group_send)(
#                 f'chat_{room_name}',
#                 {
#                     'type': 'chat.message',
#                     'message': serializer.validated_data['message'],
#                     'user_id': serializer.validated_data['user_id'],
#                 }
#             )
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # class ReceivedMessagesView(generics.ListAPIView):
# #     serializer_class = ChatMessageSerializer

# #     def get_queryset(self):
# #         user_id = self.kwargs['user_id']  # Get the user_id from the URL parameter
# #         # You can customize the queryset to filter messages for the specified user
# #         return ChatMessage.objects.filter(sender=user_id)

# chat/views.py

from rest_framework import viewsets
from .models import UserProfileModel, ChatModel, ChatNotification
from .serializers import UserProfileSerializer, ChatModelSerializer, ChatNotificationSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer

class ChatModelViewSet(viewsets.ModelViewSet):
    queryset = ChatModel.objects.all()
    serializer_class = ChatModelSerializer

class ChatNotificationViewSet(viewsets.ModelViewSet):
    queryset = ChatNotification.objects.all()
    serializer_class = ChatNotificationSerializer
