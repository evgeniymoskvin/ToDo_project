from django.shortcuts import render, redirect
from django.views import View
from .forms import TodoForm
from todo_api import views as api_v


class IndexView(View):
    def get(self, request):
        api_data = api_v.ToDOapiView().get_queryset()
        content = {'api_data': api_data,
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
        api_detail = api_v.ToDoDetailView().get(request, pk=pk)
        content = {'api_detail': api_detail,
                   'user': request.user}
        return render(request, 'todo_manager/details.html', content)
