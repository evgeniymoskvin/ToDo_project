from .models import ToDoModel
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, Select, SelectDateWidget, SplitDateTimeWidget
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
                   "time_field": SplitDateTimeWidget()
                   }
