# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        receiver_id = text_data_json['receiver_id']

        # You should add authentication logic here to verify users and their permissions

        # Save the message to the database
        sender = self.scope["user"]
        message = Message.objects.create(sender=sender, receiver_id=receiver_id, content=message)

        # Send the message to the receiver's WebSocket
        receiver_channel_name = f"user_{receiver_id}"
        await self.channel_layer.send(
            receiver_channel_name,
            {
                "type": "chat.message",
                "message": message.content,
                "sender": sender.username,
            },
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))
