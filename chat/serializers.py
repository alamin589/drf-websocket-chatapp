# chat/serializers.py
from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    user_id = serializers.CharField()