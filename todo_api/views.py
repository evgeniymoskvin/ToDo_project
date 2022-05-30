from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView, UpdateAPIView
from todo_manager.models import ToDoModel, Comments
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers, filters
from django.shortcuts import get_object_or_404
from rest_framework import status


class ToDOapiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = serializers.TaskSerializer


    def filter_queryset(self, queryset):
        queryset = filters.author_id_filter(queryset, author_id=self.request.query_params.get("author_id"))
        queryset = filters.important_filter(queryset, important=self.request.query_params.get("important"))
        queryset = filters.public_filter(queryset, public=self.request.query_params.get("public"))
        return queryset.order_by("important").order_by("status")


class ToDOPublicapiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)


# class ToDoDetailView(RetrieveAPIView, UpdateAPIView):
#     queryset = ToDoModel.objects.all()
#     serializer_class = serializers.DetailTaskSerializer

class ToDoDetailView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(ToDoModel, pk=pk)
        return Response(serializers.DetailTaskSerializer(instance=todo).data)

    def patch(self, request, pk):
        todo = get_object_or_404(ToDoModel, pk=pk)
        ser = serializers.TaskSerializer(instance=todo, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        todo = ToDoModel.objects.get(pk=pk)
        if todo.author == request.user:
            ser.save(author=request.user)
            return Response(ser.data)
        else:
            return Response(data="Вы не можете изменять заметку", status=status.HTTP_400_BAD_REQUEST)


class CommentsView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentSerializer

#
# class ToDoAuthorAPIView(ListAPIView):
#     queryset = ToDoModel.objects.all()
#     serializer_class = serializers.TaskSerializer


