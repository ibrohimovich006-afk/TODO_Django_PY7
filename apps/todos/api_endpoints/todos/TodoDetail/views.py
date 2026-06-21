from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from apps.todos.api_endpoints.todos.TodoDetail.serializers import TodoDetailSerializer
from apps.todos.models import Todo


# @api_view(['GET'])
# def todo_detail_view(request, pk):
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response({'error': 'Todo not found'}, status=404)

#     serializer = TodoDetailSerializer(todo)
#     return Response(serializer.data)


class TodoDetailAPIView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer