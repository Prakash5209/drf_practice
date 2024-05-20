from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from todo.serializers import TodoModelSerializer
from todo.models import TodoModel

class TodoModelView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="get list of",
        responses={200: TodoModelSerializer(many=True)},
        security=[{'Bearer':[]}]
    )
    def get(self,request):
        queryset = TodoModel.objects.filter(user=request.user)
        serializer = TodoModelSerializer(queryset,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="get list of",
        request_body = TodoModelSerializer,
        responses={200: TodoModelSerializer(many=True)},
        security=[{'Bearer':[]}]
    )

    def post(self,request):
        serializer = TodoModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


#class TodoModelDetailView(APIView):
#    def get(self,request,pk):
#        queryset = TodoModel.objects.get(id = pk)
#        serializer = TodoModelSerializer(queryset)
#        return Response(serializer.data,status=status.HTTP_200_OK)
#    
#    def post(self,request,pk):
#        queryset = TodoModel.objects.get(id = pk)
#        serializer = TodoModelSerializer(instance = queryset,data = request.data)
#        if serializer.is_valid():
#            serializer.save(user=self.request.user)
#            return Response(serializer.data,status = status.HTTP_201_CREATED)
#        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


#class TodoModelView(APIView):
#    permission_classes = [IsAuthenticated]
#
#    @swagger_auto_schema(
#        operation_description="Get list of TODO items for the authenticated user",
#        responses={200: TodoModelSerializer(many=True)},
#        security=[{'Bearer': []}]
#    )
#    def get(self, request):
#        queryset = TodoModel.objects.filter(user=request.user)
#        serializer = TodoModelSerializer(queryset, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#
#    @swagger_auto_schema(
#        operation_description="Create a new TODO item for the authenticated user",
#        request_body=TodoModelSerializer,
#        responses={201: TodoModelSerializer()},
#        security=[{'Bearer': []}]
#    )
#    def post(self, request):
#        serializer = TodoModelSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save(user=request.user)
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoModelDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a TODO item by ID",
        responses={200: TodoModelSerializer()},
        security=[{'Bearer': []}]
    )
    def get(self, request, pk):
        queryset = TodoModel.objects.get(id=pk)
        serializer = TodoModelSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update a TODO item by ID",
        request_body=TodoModelSerializer,
        responses={200: TodoModelSerializer()},
        security=[{'Bearer': []}]
    )
    def put(self, request, pk):
        queryset = TodoModel.objects.get(id=pk)
        serializer = TodoModelSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a TODO item by ID",
        request_body=TodoModelSerializer,
        responses={200: TodoModelSerializer()},
        security=[{'Bearer': []}]
    )
    def patch(self, request, pk):
        queryset = TodoModel.objects.get(id=pk)
        serializer = TodoModelSerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a TODO item by ID",
        responses={204: 'No Content'},
        security=[{'Bearer': []}]
    )
    def delete(self, request, pk):
        queryset = TodoModel.objects.get(id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
