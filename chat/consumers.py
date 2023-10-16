import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from registration.models import User
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from registration.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']  # Get user_id from URL route

        # Authenticate the user asynchronously
        self.user = await self.get_user(self.user_id)

        if self.user is not None:
            # Accept the WebSocket connection if the user is authenticated
            await self.accept()
        else:
            # Reject the connection if the user is not authenticated
            await self.close()

    async def disconnect(self, close_code):
        # Handle disconnect (you can implement logic for disconnection here)
        pass

    async def receive(self, text_data):
        # Handle incoming messages from the WebSocket (implement your logic here)
        message_data = json.loads(text_data)

        # Extract user_id and message text from the message
        message_text = message_data.get('message')

        # Handle the message with user_id
        # Implement your message handling logic here, e.g., saving to the database or broadcasting to other users

        # For demonstration purposes, we'll just echo the message back to the sender
        await self.send(text_data=json.dumps({'message': message_text, 'user_id': self.user_id}))

    @database_sync_to_async
    def get_user(self, user_id):
        try:
            # Query the database to retrieve the user with the given user_id
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            # Return None if the user does not exist
            return None

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
#         message_data = json.loads(text_data)
#         user_id = message_data.get('user_id')
#         message_text = message_data.get('message')

#         # Handle the message with user_id
#         # Implement your message handling logic here, e.g., saving to the database or broadcasting to other users

#         # For demonstration purposes, we'll just echo the message back to the sender
#         await self.send(text_data=json.dumps({'message': message_text, 'user_id': user_id}))


#     @database_sync_to_async
#     def get_user(self, user_id):
#         try:
#             # Query the database to retrieve the user with the given user_id
#             return User.objects.get(user_id=user_id)
#         except User.DoesNotExist:
#             # Return None if the user does not exist
#             return None
