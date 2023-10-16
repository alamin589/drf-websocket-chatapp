# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user_id = self.scope['url_route']['kwargs']['user_id']

#         # Authenticate the user (You may have your own authentication logic)
#         if self.user_id == 1:
#             await self.accept()
#         else:
#             await self.close()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Check if the user_id is valid (for demo, we only accept user_id=1)
#         if self.user_id == 1:
#             # For simplicity, let's assume we want to send to user_id=2
#             await self.send_message(user_id=2, message=message)

#     @database_sync_to_async
#     def send_message(self, user_id, message):
#         # You can implement your own logic to find the WebSocket connection for the target user
#         # For simplicity, we'll just send to the same channel as user_id
#         async_to_sync(self.channel_layer.group_add)(str(user_id), self.channel_name)
#         async_to_sync(self.channel_layer.group_send)(
#             str(user_id),
#             {
#                 'type': 'chat.message',
#                 'message': message
#             }
#         )

#     async def chat_message(self, event):
#         message = event['message']
#         await self.send(text_data=json.dumps({'message': message}))
