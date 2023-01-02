from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UsersData
from .serializers import UsersDataSerializer
from rest_framework.parsers import JSONParser 


class ContentView(APIView):
    def get(self, request):
        data = UsersData.objects.all()
        cleaned_data = [i for i in data if request.user.pk == i.owner.pk]
        serializer = UsersDataSerializer(cleaned_data, context={'request': request}, many=True)
        return Response(serializer.data)

class CertainDataView(APIView):
    def get(self, request, pk):
        data = UsersData.objects.get(pk=pk)
        serializer = UsersDataSerializer(data, context={'request': request}, many=False)
        if request.user.pk == data.owner.pk:
            return Response(serializer.data)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateView(APIView): 
    def post(self, request):
        owner = request.user.pk
        data = request.data
        data["owner"] = owner
        serializer = UsersDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateView(APIView):
    def put(self, request, pk):
        try:
            owner = request.user.pk
            user = UsersData.objects.get(pk=pk)
            updated = JSONParser().parse(request) 
            updated["owner"] = owner
            if request.user.pk == user.owner.pk: 
                serializer = UsersDataSerializer(user, data=updated)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
            else:
                raise UsersData.DoesNotExist
        except UsersData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteView(APIView):
    def delete(self, request, pk):
        try:
            data = UsersData.objects.get(pk=pk)
            if request.user.pk == data.owner.pk:
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise UsersData.DoesNotExist
        except UsersData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)