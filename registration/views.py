from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # In a production system, you should hash the password before saving.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # In a production system, you should verify the password (e.g., by hashing and comparing).
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=400)

        return Response({'message': 'Login successful'}, status=200)
    
    

