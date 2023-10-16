# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async

# from registration.models import User

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Get the user_id from the URL and use it to authenticate the user
#         user_id = self.scope['url_route']['kwargs']['user_id']  # Get user_id from URL route

#         # Authenticate the user by querying the database asynchronously
#         user = await self.get_user(user_id)

#         if user is not None:
#             # Accept the WebSocket connection if the user is authenticated
#             await self.accept()
#         else:
#             # Reject the connection if the user is not authenticated
#             await self.close()

#     async def disconnect(self, close_code):
#         # Handle disconnect (you can implement logic for disconnection here)
#         pass

#     async def receive(self, text_data):
#         # Handle incoming messages from the WebSocket (implement your logic here)
#         await self.send(text_data)

#     @database_sync_to_async
#     def get_user(self, user_id):
#         try:
#             # Query the database to retrieve the user with the given user_id
#             return User.objects.get(user_id=user_id)
#         except User.DoesNotExist:
#             # Return None if the user does not exist
#             return None
# consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Get user_id from the URL, for example: /ws/chat/1/
#         self.user_id = self.scope['url_route']['kwargs']['user_id']

#         # Check if the user is authorized to connect (you need to implement your own authorization logic here)

#         await self.accept()

#     async def disconnect(self, close_code):
#         pass 

#     async def receive(self, text_data):
#         # Receive a message from the WebSocket
#         data_json = json.loads(text_data)
#         message = data_json['message']

#         # Determine the recipient's user_id (e.g., from the URL or message data)
#         recipient_user_id = data_json['recipient_user_id']

#         # Send the message to the recipient user's WebSocket
#         await self.send_message_to_user(message, recipient_user_id)

#     async def send_message_to_user(self, message, recipient_user_id):
#         # Use UserProfile or User model to find the recipient's WebSocket
#         try:
#             recipient_user = User.objects.get(user_id=recipient_user_id)
#             recipient_channel_name = recipient_user.userprofile.chatconsumer.channel_name

#             await self.channel_layer.send(
#                 recipient_channel_name,
#                 {
#                     'type': 'chat.message',
#                     'message': message,
#                 }
#             )
#         except User.DoesNotExist:
#             # Handle the case where the recipient user doesn't exist
#             pass

#     async def chat_message(self, event):
#         # Send a message to the WebSocket
#         message = event['message']
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from registration.models import User, UserProfile

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user_id = self.scope['url_route']['kwargs']['user_id']
#         self.user = await self.get_user(self.user_id)

#         if self.user:
#             await self.accept()
#         else:
#             await self.close()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']
#         receiver_id = data['receiver_id']

#         if not self.user or not message or not receiver_id:
#             return

#         receiver = await self.get_user(receiver_id)
#         if not receiver:
#             return

#         await self.send_message(message, receiver_id)

#     async def send_message(self, message, receiver_id):
#         await self.send(text_data=json.dumps({
#             'message': message,
#             'sender_id': self.user_id,
#             'receiver_id': receiver_id,
#         }))

#     async def get_user(self, user_id):
#         try:
#             return User.objects.get(user_id=user_id)
#         except User.DoesNotExist:
#             return None
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.core import serializers

from registration.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope['url_route']['kwargs']['user_id']
        self.user = await self.get_user(user_id)

        if self.user is not None:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        recipient_id = text_data_json['recipient_id']

        # Check if the recipient exists
        recipient = await self.get_user(recipient_id)

        if recipient:
            # Send the message to the recipient's WebSocket
            await self.send({
                'type': 'chat.message',
                'message': message,
                'sender_id': self.user.id,
                'recipient_id': recipient_id,
            })

    @database_sync_to_async
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
