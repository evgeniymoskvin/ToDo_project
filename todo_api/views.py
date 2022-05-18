from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from todo_manager.models import ToDoModel, Comments
from . import serializers


class ToDOapiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)


class ToDoDetailView(APIView):
    def get(self, request, pk):
        note = get_object_or_404(ToDoModel, pk=pk)
        serializer = serializers.TaskSerializer(instance=note, )
        return serializer.data
