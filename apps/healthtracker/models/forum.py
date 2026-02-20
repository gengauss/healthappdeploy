from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    class Meta:
        db_table = 'question'
        get_latest_by = 'created'
    title = models.CharField(max_length=200)
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)


class Comment(models.Model):
    class Meta:
        db_table = 'comment'
        get_latest_by = 'created'
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)


# admin.site.register(Question, Comment)
