from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.todos.api_endpoints.todos.TodoList.serializers import TodoListSerializer
from apps.todos.models import Todo


# @api_view(['GET'])
# def todo_list_view(request):
#     todos = Todo.objects.all()
#     serializer = TodoListSerializer(todos, many=True)
#     return Response(serializer.data)


class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status='Yangi')
        return queryset