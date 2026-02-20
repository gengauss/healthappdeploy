from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from apps.healthtracker.models import Profile


class Goal(models.Model):
    class Meta:
        db_table = 'goal'
        get_latest_by = 'created'

    title = models.CharField(max_length=256, default="当ウェブサイトをご利用いただきありがとうございます。 登録プロセスが完了しました。")
    complete = models.BooleanField(default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, default="2020-01-01 00:00:00")
    person_of = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


admin.site.register(Goal)
