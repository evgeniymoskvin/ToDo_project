from .models import ToDoModel, Comments
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, Select
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime

class TodoForm(ModelForm):
    class Meta:
        model = ToDoModel
        exclude = ['author']
        # fields = ["author", "title", 'message', 'important', 'public', 'status']
        widgets = {"title": TextInput(attrs={"placeholder": "Введите текст",
                                             "class": "form-control"}),
                   "message": Textarea(attrs={"placeholder": "Введите текст",
                                              "class": "form-control"}),
                   "important": CheckboxInput(),
                   "public": CheckboxInput(),
                   "status": Select(attrs={'class': "btn btn-first dropdown-toggle"}),
                   }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = {"comment"}
        widgets = {"comment": Textarea(attrs={"placeholder": "Введите комментарий",
                                              "class": "form-control"})}
