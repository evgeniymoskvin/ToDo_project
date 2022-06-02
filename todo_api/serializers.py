from rest_framework import serializers

from todo_manager.models import ToDoModel, Comments
from datetime import datetime


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoModel
        fields = "__all__"
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class CommentSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = ('author',)

class DetailTaskSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoModel
        fields = ("title", "message", "status", "author", "comments",)


class QueryParamsTaskFilterSerializer(serializers.Serializer):
    status = serializers.ListField(child=serializers.ChoiceField(choices=ToDoModel.StatusNote.choices), required=False)
