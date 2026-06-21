from rest_framework import serializers

from apps.todos.models import Todo


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'