from rest_framework import serializers
from todo_manager.models import ToDoModel, Comments
from datetime import datetime



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoModel
        exclude = ('public',)
        read_only_fields = ('author',)
