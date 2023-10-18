# chat/serializers.py
# chat/serializers.py

from rest_framework import serializers
from .models import UserProfileModel, ChatModel, ChatNotification

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = '__all__'

class ChatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = '__all__'

class ChatNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatNotification
        fields = '__all__'
