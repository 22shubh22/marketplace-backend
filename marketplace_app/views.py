from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
)
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView(TokenObtainPairView, APIView):
    """
    Login POST API
        Service usage and description : This API is used to log in the user, generatin an access and refresh token.
        Authentication Required : NO
        Data : {
            "username" : username,
            "password" : password
        }
        Response : {
            "message" : "Login successful.",
            "account_id": account_id,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    """
    def post(self, request, format=None):
        data = request.data
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, )
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)