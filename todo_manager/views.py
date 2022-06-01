from django.shortcuts import render, redirect
from django.views import View
from .forms import TodoForm, CommentForm
from todo_api import views as api_v
from .models import ToDoModel, Comments
from django.http import HttpRequest
from django.views.generic import UpdateView

from django.http.response import HttpResponseRedirect


class IndexView(View):
    def get(self, request):
        data_public = ToDoModel.objects.get_queryset().filter(public=True)
        data_all = ToDoModel.objects.get_queryset()
        content = {'data_public': data_public,
                   'data_all': data_all,
                   'user': request.user}
        return render(request, 'todo_manager/index.html', content)


class AboutView(View):
    def get(self, request: HttpRequest):
        content = {'user': request.user,
                   'server': request.get_host(),
                   'request': request}
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
            return redirect(request.META['HTTP_REFERER'])


class DetailViewsDelete(View):

    def get(self, request, pk):
        post_del = ToDoModel.objects.get(pk=pk)
        if post_del.author == request.user:
            post_del.delete()
        return redirect('index')


class NoteMyView(View):
    def get(self, request):
        obj = ToDoModel.objects.all()
        content = {'obj': obj.filter(author=request.user),
                   'user': request.user
                   }
        return render(request, 'todo_manager/user_notes.html', content)


class UpdateViewDetail(UpdateView):
    model = ToDoModel
    template_name = 'todo_manager/add_note.html'
    form_class = TodoForm

