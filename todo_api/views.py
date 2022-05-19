from rest_framework.generics import ListAPIView, GenericAPIView
from todo_manager.models import ToDoModel, Comments
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


class ToDOapiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)


class ToDoDetailView(ListAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = ToDoModel.objects.all()

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = super().get_queryset()
        return queryset.filter(id=pk)

    def get_data(self, request, pk):
        note = ToDoModel.objects.get(pk=pk)
        serializer = serializers.TaskSerializer(instance=note, )
        return serializer.data



