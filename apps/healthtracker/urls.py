from django.contrib.auth import views as auth_views
from django.urls import path

from .views import healthtracker, goal, forum
from .views.healthtracker import select_food, update_food, delete_food, ProfilePage, add_food

urlpatterns = [
    path('', healthtracker.index, name="healthtracker"),
    path('register', healthtracker.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='healthtracker/login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='healthtracker/logout.html'), name="logout"),

    path('caloriestracker', healthtracker.calories_tracker, name="caloriestracker"),
    path('caloriestracker/select_food/', select_food, name='select_food'),
    path('caloriestracker/add_food/', add_food, name='add_food'),
    path('caloriestracker/update_food/<str:pk>/', update_food, name='update_food'),
    path('caloriestracker/delete_food/<str:pk>/', delete_food, name='delete_food'),
    path('caloriestracker/profile/', ProfilePage, name='profile'),
    path('goalstracker', goal.listGoal, name="goalstracker"),
    path('goalstracker/update_goal/<str:pk>/', goal.updateGoal, name="update_goal"),
    path('goalstracker/delete_goal/<str:pk>/', goal.deleteGoal, name="delete_goal"),

    path('forum', forum.index, name="forum"),
    path('forum/<int:question_id>/', forum.detail, name='detail'),
    path('forum/<int:question_id>/delete', forum.delete, name='delete'),
    path('forum/<int:question_id>/update', forum.update, name='update'),
    path('forum/<int:question_id>/like', forum.like, name='like')
]
