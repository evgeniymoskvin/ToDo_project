from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView, UpdateAPIView
from todo_manager.models import ToDoModel, Comments
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


class ToDOapiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = serializers.TaskSerializer


class ToDOPublicapiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)


class ToDoDetailView(UpdateAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = ToDoModel.objects.all()
