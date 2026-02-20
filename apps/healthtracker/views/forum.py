from django.shortcuts import render, redirect
from django.http import Http404
from django.utils import timezone

from ..models import Question, Comment


def index(request):
    if request.method == 'POST':
        question = Question(title=request.POST['title'], text=request.POST['text'], posted_at=timezone.now())
        question.save()
    questions = Question.objects.order_by('-posted_at')
    context = {
        'questions': questions
    }
    return render(request, '../templates/forum/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    if request.method == 'POST':
        comment = Comment(question=question, text=request.POST['text'], posted_at=timezone.now())
        comment.save()

    context = {
        'question': question,
        'comments': question.comments.order_by('-posted_at')
    }
    return render(request, '../templates/forum/detail.html', context)


def update(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    if request.method == 'POST':
        question.title = request.POST['title']
        question.text = request.POST['text']
        question.save()
        return redirect(detail, question_id)

    context = {
        'question': question
    }
    return render(request, '../templates/forum/edit.html', context)


def delete(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Article does not exist")

    question.delete()
    return redirect(index)


def like(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        question.like += 1
        question.save()
    except Question.DoesNotExist:
        raise Http404("Article does not exist")

    return redirect(detail, question_id)
