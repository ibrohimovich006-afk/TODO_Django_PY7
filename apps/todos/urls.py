from django.urls import path

from apps.todos.api_endpoints.todos.TodoCreate.views import TodoCreateAPIView
from apps.todos.api_endpoints.todos.TodoDetail.views import TodoDetailAPIView
from apps.todos.api_endpoints.todos.TodoDetail.views import TodoDetailAPIView
from apps.todos.api_endpoints.todos.TodoUpdateDestory.views import todo_update_destroy_view
from apps.todos.api_endpoints.todos.TodoList.views import TodoListAPIView


urlpatterns = [
    path('', TodoListAPIView.as_view(), name='todo-list'),
    path('create/', TodoCreateAPIView.as_view(), name='todo-create'),
    path('<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
    path('<int:pk>/update/', todo_update_destroy_view, name='todo-update'),
    path('<int:pk>/delete/', todo_update_destroy_view, name='todo-delete'),
]