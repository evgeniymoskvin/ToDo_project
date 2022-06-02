import datetime

from django.db import models
from datetime import date, timedelta, datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


def get_date():
    return datetime.now() + timedelta(days=1)


class ToDoModel(models.Model):
    """Статусы и записи"""

    class StatusNote(models.IntegerChoices):  # Выбор статуса задачи
        ACTIVE = 1, _('Активно')
        POSTPONED = 2, _('Отложено')
        DONE = 3, _('Выполнено')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("Заголовок"), max_length=150)
    message = models.TextField("Текст заметки", max_length=5000)
    status = models.IntegerField(verbose_name="Статус", default=StatusNote.ACTIVE, choices=StatusNote.choices)
    important = models.BooleanField("Важно", default=False)
    public = models.BooleanField("Публично", default=False)
    time_field = models.DateTimeField(verbose_name="Дата", default=get_date)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/details/{self.id}'

    class Meta:
        verbose_name = _("Задача")  # todo с маленькой буквы
        verbose_name_plural = _("Задачи")


class Comments(models.Model):
    comment = models.TextField("Текст комментария", max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    todo_post = models.ForeignKey(ToDoModel, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments",
                                  default=None)

    def __str__(self):
        return f'{self.author.username}: {self.comment[:25]}'

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")
