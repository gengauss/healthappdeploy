from django.urls import path
from .views import visualization

urlpatterns = [
    path('', visualization.index, name="visualization"),
    path('surveyresult', visualization.survey_result, name='surveyresult'),
    path('diabetes', visualization.diabetes_result, name='diabetes'),
    path('depression', visualization.depression_result, name='depression'),
    path('suiciderate', visualization.suicide_result, name='suiciderate'),
]
