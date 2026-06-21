from django.shortcuts import render

from apps.todos.models import Todo


def get_todos(request):
    todos = Todo.objects.all()
    print(todos)
    return render(request, 'todos/list.html', {'todos': todos})
