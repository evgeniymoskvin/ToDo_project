from django.shortcuts import render, redirect
from django.views import View
from .forms import TodoForm, CommentForm
from todo_api import views as api_v
from .models import ToDoModel, Comments


class IndexView(View):
    def get(self, request):
        api_data_public = api_v.ToDOPublicapiView().get_queryset()
        api_data_all = api_v.ToDOapiView().get_queryset()
        content = {'api_data_public': api_data_public,
                   'api_data_all': api_data_all,
                   'user': request.user}
        return render(request, 'todo_manager/index.html', content)


class AboutView(View):
    def get(self, request):
        content = {'user': request.user,
                   'server': request.get_host()}
        return render(request, 'todo_manager/about.html', content)


class AddNoteView(View):
    def get(self, request):
        form = TodoForm()
        context = {'form': form,
                   'user': request.user}
        return render(request, 'todo_manager/add_note.html', context)

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            form.save()
            return redirect('index')


class DetailViews(View):
    def get(self, request, pk):
        obj = ToDoModel.objects.get(pk=pk)
        comments = Comments.objects.all()
        comments_filter = comments.filter(todo_post_id=pk)
        form = CommentForm(request.POST)
        content = {'obj': obj,
                   'user': request.user,
                   'form': form,
                   'comments': comments_filter}
        return render(request, 'todo_manager/details.html', content)

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.todo_post_id = pk
            form.save()
            obj = ToDoModel.objects.get(pk=pk)
            content = {'obj': obj,
                       'user': request.user,
                       'form': form}
            return render(request, 'todo_manager/details.html', content)
