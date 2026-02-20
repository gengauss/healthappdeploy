from datetime import date, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from ..forms import UserRegisterForm, AddFoodForm, ProfileForm, SelectFoodForm
from ..models import Profile, PostFood, Food
from apps.healthtracker.filters import FoodFilter


@login_required(login_url='login')
def index(request):
    person = Profile.objects.filter(person_of=request.user).last()
    return render(request, '../templates/healthtracker/index.html', {'person': person})


def register(request):
    if request.user.is_authenticated:
        return redirect('../templates/healthtracker/index.html')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {user}!')
                return redirect('login')
        return render(request, '../templates/healthtracker/register.html', {'form': form})


def forum(request):
    return render(request, '../templates/healthtracker/forum.html', {})


def calories_tracker(request):
    # taking the latest profile object
    calories = Profile.objects.filter(person_of=request.user).last()
    calorie_goal = calories.calorie_goal

    # creating one profile each day
    if date.today() > calories.date:
        profile = Profile.objects.create(person_of=request.user)
        profile.save()

    calories = Profile.objects.filter(person_of=request.user).last()

    # showing all food consumed present day

    all_food_today = PostFood.objects.filter(profile=calories)

    calorie_goal_status = calorie_goal - calories.total_calorie
    over_calorie = 0
    if calorie_goal_status < 0:
        over_calorie = abs(calorie_goal_status)

    context = {
        'total_calorie': calories.total_calorie,
        'calorie_goal': calorie_goal,
        'calorie_goal_status': calorie_goal_status,
        'over_calorie': over_calorie,
        'food_selected_today': all_food_today
    }
    return render(request, '../templates/healthtracker/caloriestracker.html', context)


# for selecting food each day
@login_required
def select_food(request):
    person = Profile.objects.filter(person_of=request.user).last()
    # for showing all food items available
    food_items = Food.objects.filter(person_of=request.user)
    form = SelectFoodForm(request.user, instance=person)

    if request.method == 'POST':
        form = SelectFoodForm(request.user, request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('caloriestracker')
    else:
        form = SelectFoodForm(request.user)

    context = {'form': form, 'food_items': food_items}
    return render(request, '../templates/healthtracker/select_food.html', context)


# for adding new food
def add_food(request):
    # for showing all food items available
    food_items = Food.objects.filter(person_of=request.user)
    form = AddFoodForm(request.POST)
    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.person_of = request.user
            profile.save()
            return redirect('add_food')
    else:
        form = AddFoodForm()

    # for filtering food
    myFilter = FoodFilter(request.GET, queryset=food_items)
    food_items = myFilter.qs
    context = {'form': form, 'food_items': food_items, 'myFilter': myFilter}
    return render(request, '../templates/healthtracker/add_food.html', context)


# for updating food given by the user
@login_required
def update_food(request, pk):
    food_items = Food.objects.filter(person_of=request.user)

    food_item = Food.objects.get(id=pk)
    form = AddFoodForm(instance=food_item)
    if request.method == 'POST':
        form = AddFoodForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('profile')
    myFilter = FoodFilter(request.GET, queryset=food_items)
    context = {'form': form, 'food_items': food_items, 'myFilter': myFilter}

    return render(request, '../templates/healthtracker/add_food.html', context)


# for deleting food given by the user
@login_required
def delete_food(request, pk):
    food_item = Food.objects.get(id=pk)
    if request.method == "POST":
        food_item.delete()
        return redirect('profile')
    context = {'food': food_item, }
    return render(request, '../templates/healthtracker/delete_food.html', context)


# profile page of user
@login_required
def ProfilePage(request):
    # getting the lastest profile object for the user
    person = Profile.objects.filter(person_of=request.user).last()
    food_items = Food.objects.filter(person_of=request.user)
    form = ProfileForm(instance=person)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=person)

    # querying all records for the last seven days
    some_day_last_week = timezone.now().date() - timedelta(days=7)
    records = Profile.objects.filter(date__gte=some_day_last_week, date__lt=timezone.now().date(),
                                     person_of=request.user)

    context = {'form': form, 'food_items': food_items, 'records': records}
    return render(request, '../templates/healthtracker/profile.html', context)


def goals(request):
    return render(request, '../templates/healthtracker/goalstracker.html', {})

