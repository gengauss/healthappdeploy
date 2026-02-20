from django.contrib import admin
from django.db import models


class Survey(models.Model):
    class Meta:
        db_table = 'surveys'
        get_latest_by = 'created'

    timestamp = models.DateTimeField()
    # General
    country = models.CharField(max_length=256, null=True, blank=True)
    age = models.CharField(max_length=256, null=True, blank=True)
    occupation = models.CharField(max_length=256, null=True, blank=True)
    gender = models.CharField(max_length=256, null=True, blank=True)
    # Physical Health
    water_per_day = models.CharField(max_length=256, null=True, blank=True)
    diet = models.CharField(max_length=256, null=True, blank=True)
    no_of_meals = models.CharField(max_length=256, null=True, blank=True)
    first_meal_time = models.CharField(max_length=256, null=True, blank=True)
    last_meal_time = models.CharField(max_length=256, null=True, blank=True)
    same_time_meal = models.CharField(max_length=256, null=True, blank=True)
    do_exercise = models.CharField(max_length=256, null=True, blank=True)
    exercise_period = models.CharField(max_length=256, null=True, blank=True)
    exercise_detail = models.TextField(null=True, blank=True)
    sleep_period = models.CharField(max_length=256, null=True, blank=True)
    sleep_time = models.CharField(max_length=256, null=True, blank=True)
    wake_up_time = models.CharField(max_length=256, null=True, blank=True)
    medical_checkup = models.CharField(max_length=256, null=True, blank=True)
    chronic_issue = models.CharField(max_length=256, null=True, blank=True)
    chronic_issue_detail = models.TextField(null=True, blank=True)
    # Mental Health
    mental_important = models.IntegerField(null=True, blank=True)
    mental_effect = models.IntegerField(null=True, blank=True)
    stress = models.CharField(max_length=256, null=True, blank=True)
    stress_relief = models.TextField(null=True, blank=True)
    job_school_rate = models.IntegerField(null=True, blank=True)
    family_rate = models.IntegerField(null=True, blank=True)
    friends_rate = models.IntegerField(null=True, blank=True)
    partner_rate = models.IntegerField(null=True, blank=True)
    sns_rate = models.IntegerField(null=True, blank=True)
    money_rate = models.IntegerField(null=True, blank=True)
    depression = models.CharField(max_length=256, null=True, blank=True)
    anxiety_disorder = models.CharField(max_length=256, null=True, blank=True)
    bipolar_disorder = models.CharField(max_length=256, null=True, blank=True)
    mental_diseases = models.CharField(max_length=256, null=True, blank=True)
    mental_detail = models.TextField(null=True, blank=True)


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'country', 'age', 'occupation', 'gender')


admin.site.register(Survey, SurveyAdmin)
