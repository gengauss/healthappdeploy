from django.contrib import admin
from django.db import models


class SuicideRate(models.Model):
    class Meta:
        db_table = 'suicide_rate'
        get_latest_by = 'created'

    country = models.CharField(max_length=256, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    suicides_no = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    suicides_100kpo = models.FloatField(null=True, blank=True)
    country_year = models.CharField(max_length=50, null=True, blank=True)
    HDI_year = models.FloatField(null=True, blank=True)
    gdp_year = models.IntegerField(null=True, blank=True)
    gdp_per_capital = models.IntegerField(null=True, blank=True)
    generation = models.CharField(max_length=256, null=True, blank=True)


class SuicideRateAdmin(admin.ModelAdmin):
    list_display = ('country', 'year', 'sex', 'age', 'suicides_no', 'population', 'suicides_100kpo', 'country_year',
                    'HDI_year', 'gdp_year', 'gdp_per_capital', 'generation')


admin.site.register(SuicideRate, SuicideRateAdmin)
