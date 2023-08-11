from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def list_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True) 
    message = f'Используется метод <{request.method}>'
    return Response({'todos': serializer.data, 'message': message})


@api_view(['POST'])
def create_todos(request):
    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        message = f'Используется метод <{request.method}>'
        serializer.save()
        return Response({'Post': serializer.data, 'message': message})
    

@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    message = f'Используется метод <{request.method}>'
    return Response({'Успешно удалён пост №': pk, 'message': message})


@api_view(['PATCH'])
def update_todos(request, primary_key):
    todo = get_object_or_404(Todo, id=primary_key)
    serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        message = f'Используется метод <{request.method}>'
        return Response({'Обновлен пост №': serializer.data, 'message': message})