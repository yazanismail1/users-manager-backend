import requests
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UsersData
from .serializers import UsersDataSerializer


class ContentView(APIView):
    def get(self, request):
        data = UsersData.objects.all()
        serializer = UsersDataSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

class CertainDataView(APIView):
    def get(self, request, pk):
        data = UsersData.objects.get(pk=pk)
        serializer = UsersDataSerializer(data, context={'request': request}, many=False)
        print(serializer.data)
        return Response(serializer.data)

class CreateView(APIView):
    def post(self, request):
        serializer = UsersDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateView(APIView):
    def put(self, request, pk):
        try:
            user = UsersData.objects.get(pk=pk)
            serializer = UsersDataSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        except UsersData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteView(APIView):
    def delete(self, request, pk):
        try:
            data = UsersData.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UsersData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)