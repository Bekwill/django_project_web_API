from rest_framework.decorators import api_view
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework import response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated




@api_view(['POST'])
def register(request):
    if request.user.is_authenticated:
        return response(status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return response(status=status.HTTP_201_CREATED)

    return response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        if request.user.is_authenticated:
            return response(status.HTTP_400_BAD_REQUEST)
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return response(data=serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return response(data={'errors': 'invalid authentications'},status=status.HTTP_400_BAD_REQUEST)

        Login(request, user)
        return response(status.HTTP_200_OK)

class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        logout(request)
        return response(status.HTTP_200_OK)




