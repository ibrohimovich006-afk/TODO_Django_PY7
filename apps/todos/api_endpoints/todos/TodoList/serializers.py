from rest_framework import serializers

from apps.todos.models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'