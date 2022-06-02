from rest_framework.generics import ListAPIView, ListCreateAPIView
from todo_manager.models import ToDoModel, Comments
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers, filters
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from django_filters.rest_framework import DjangoFilterBackend


class ToDOapiView(ListCreateAPIView):
    queryset = ToDoModel.objects.all()
    serializer = serializers.TaskSerializer
    serializer_class = serializers.TaskSerializer
    # filter_backends = [DjangoFilterBackend]

    def post(self, request, *args, **kwargs):
        serializer = serializers.TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def filter_queryset(self, queryset):
        query_params = serializers.QueryParamsTaskFilterSerializer(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)
        list_status = query_params.data.get("status")
        if list_status:
            queryset = queryset.filter(status__in=query_params.data["status"])

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
            return Response(data="Вы не можете изменять заметку", status=status.HTTP_403_FORBIDDEN)




class CommentsView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentSerializer

