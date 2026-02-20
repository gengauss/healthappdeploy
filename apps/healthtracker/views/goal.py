import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..models import Goal
from ..forms import GoalForm, UpdateForm


@login_required
def listGoal(request):
    queryset = Goal.objects.order_by('complete', 'due').filter(person_of=request.user)
    form = GoalForm()
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.person_of = request.user
            goal.save()
        return redirect('goalstracker')

    context = {
        'goals': queryset,
        'form': form,
    }
    return render(request, '../templates/healthtracker/goalstracker.html', context)


@login_required
def updateGoal(request, pk):
    queryset = Goal.objects.get(id=pk)
    form = UpdateForm(instance=queryset)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('goalstracker')

    context = {
        'form': form
    }

    return render(request, '../templates/healthtracker/update_goal.html', context)


@login_required
def deleteGoal(request, pk):
    queryset = Goal.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('goalstracker')

    context = {
        'item': queryset
    }
    return render(request, '../templates/healthtracker/delete_goal.html', context)
