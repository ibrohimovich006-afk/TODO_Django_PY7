from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from apps.todos.api_endpoints.todos.TodoDetail.serializers import TodoDetailSerializer
from apps.todos.models import Todo


@api_view(['PATCH', 'DELETE'])
def todo_update_destroy_view(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=404)

    if request.method == 'PATCH':
        serializer = TodoDetailSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            todo = serializer.save()
            return Response(TodoDetailSerializer(todo).data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)