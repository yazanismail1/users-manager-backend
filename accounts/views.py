import requests
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
# from rest_framework import generics


class SignInView(APIView):
    def post(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(data=request.data)
        if request.data.username in users.username:
            print("hiiiiiiiiii")
        # return Response()

class SignUpView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

