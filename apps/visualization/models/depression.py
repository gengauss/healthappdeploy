from django.contrib import admin
from django.db import models


class Depression(models.Model):
    class Meta:
        db_table = 'depression'
        get_latest_by = 'created'

    id_num = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    education = models.IntegerField(null=True, blank=True)
    current_education_status = models.IntegerField(null=True, blank=True)
    occupation = models.IntegerField(null=True, blank=True)
    income = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    live_with = models.IntegerField(null=True, blank=True)
    plan_preg = models.IntegerField(null=True, blank=True)
    who_support = models.IntegerField(null=True, blank=True)
    number_support = models.IntegerField(null=True, blank=True)
    relationship_with_husband = models.IntegerField(null=True, blank=True)
    relationship_with_family = models.IntegerField(null=True, blank=True)
    relationship_with_friend = models.IntegerField(null=True, blank=True)
    ds1 = models.IntegerField(null=True, blank=True)
    ds2 = models.IntegerField(null=True, blank=True)
    ds3 = models.IntegerField(null=True, blank=True)
    ds4 = models.IntegerField(null=True, blank=True)
    ds5 = models.IntegerField(null=True, blank=True)
    ds6 = models.IntegerField(null=True, blank=True)
    ds7 = models.IntegerField(null=True, blank=True)
    ds8 = models.IntegerField(null=True, blank=True)
    ds9 = models.IntegerField(null=True, blank=True)
    ds10 = models.IntegerField(null=True, blank=True)
    total_ds = models.IntegerField(null=True, blank=True)


class DepressionAdmin(admin.ModelAdmin):
    list_display = ('age', 'education', 'current_education_status', 'occupation', 'income', 'status',
                    'live_with', 'plan_preg', 'who_support', 'total_ds')


admin.site.register(Depression, DepressionAdmin)
