from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from todo.serializers import TodoModelSerializer
from todo.models import TodoModel

class TodoModelView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        queryset = TodoModel.objects.filter(user=request.user)
        serializer = TodoModelSerializer(queryset,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request):
        serializer = TodoModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class TodoModelDetailView(APIView):
    def get(self,request,pk):
        queryset = TodoModel.objects.get(id = pk)
        serializer = TodoModelSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,pk):
        queryset = TodoModel.objects.get(id = pk)
        serializer = TodoModelSerializer(instance = queryset,data = request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

