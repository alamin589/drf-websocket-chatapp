import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from registration.models import User

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user_id = self.scope['url_route']['kwargs']['user_id']  # Get user_id from URL route

#         # Authenticate the user asynchronously
#         self.user = await self.get_user(self.user_id)

#         if self.user is not None:
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
#         message_data = json.loads(text_data)

#         # Extract user_id and message text from the message
#         message_text = message_data.get('message')

#         # Handle the message with user_id
#         # Implement your message handling logic here, e.g., saving to the database or broadcasting to other users

#         # For demonstration purposes, we'll just echo the message back to the sender
#         await self.send(text_data=json.dumps({'message': message_text, 'user_id': self.user_id}))

#     @database_sync_to_async
#     def get_user(self, user_id):
#         try:
#             # Query the database to retrieve the user with the given user_id
#             return User.objects.get(user_id=user_id)
#         except User.DoesNotExist:
#             # Return None if the user does not exist
#             return None





# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from registration.models import User

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Get user_id from the URL
#         self.user_id = self.scope['url_route']['kwargs']['user_id']
#         self.room_name = f"chat_{self.user_id}"

#         # Authenticate the user asynchronously
#         self.user = await self.get_user(int(self.user_id))

#         if self.user is None:
#             # If the user is not authenticated, close the connection
#             await self.close()
#         else:
#             # Join the room
#             await self.channel_layer.group_add(
#                 self.room_name,
#                 self.channel_name
#             )

#             # Accept the WebSocket connection
#             await self.accept()

#     async def disconnect(self, close_code):
#         # Leave the room
#         await self.channel_layer.group_discard(
#             self.room_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         # Receive a message from the WebSocket
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send the message to the room
#         await self.channel_layer.group_send(
#             self.room_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     async def chat_message(self, event):
#         # Send the message to the WebSocket
#         message = event['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

#     @database_sync_to_async
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(user_id=user_id)
#         except User.DoesNotExist:
#             return None

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from registration.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get user_id from the URL
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_name = f"chat_{self.user_id}"

        # Authenticate the user asynchronously
        self.user = await self.get_user(int(self.user_id))

        if self.user is None:
            # If the user is not authenticated, close the connection
            await self.close()
        else:
            # Join the room
            await self.channel_layer.group_add(
                self.room_name,
                self.channel_name
            )

            # Accept the WebSocket connection
            await self.accept()

    async def disconnect(self, close_code):
        # Leave the room
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive a message from the WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save the message to the database (example)
        self.save_message(message)

        # Send the message to the room
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user_id,
            }
        )

    async def chat_message(self, event):
        # Send the message to the WebSocket
        message = event['message']
        user_id = event['user_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'user_id': user_id,
        }))

    @database_sync_to_async
    def get_user(self, user_id):
        try:
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return None

    @database_sync_to_async
    def save_message(self, message_text):
        # You can implement your message-saving logic here
        # For example, you can save the message to the database
        # Replace this with your actual saving code
        # For demonstration purposes, we're not saving it to the database
        pass

