from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import extend_schema


from apps.todos.api_endpoints.todos.TodoCreate.serializers import TodoCreateSerializer
from apps.todos.models import Todo

# @extend_schema(request=TodoCreateSerializer)
# @api_view(['POST'])
# def todo_create(request):
#     serializer = TodoCreateSerializer(request.data)
#     if serializer.is_valid():
#         todo=serializer.save()
#         return Response(TodoCreateSerializer(todo).data,status=201)
#     return Response(serializer.errors,status=400)

class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer