from django.contrib import admin
from .models import ToDoModel, Comments


class ToDoAdmin(admin.ModelAdmin):
    list_display = ("title", "message", "time_field", "status")
    list_filter = ("status", "public", "important")


admin.site.register(ToDoModel, ToDoAdmin)
admin.site.register(Comments)
