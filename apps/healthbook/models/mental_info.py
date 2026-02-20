from django.contrib import admin
from django.db import models


class MentalInfo(models.Model):
    class Meta:
        db_table = 'mental_info'
        get_latest_by = 'created'

    name = models.CharField(max_length=256, default=None, null=True, blank=True)
    general_information = models.TextField(default=None, null=True, blank=True)
    symptoms = models.TextField(default=None, null=True, blank=True)
    diagnosis = models.TextField(default=None, null=True, blank=True)
    cause = models.TextField(default=None, null=True, blank=True)
    prevention = models.TextField(default=None, null=True, blank=True)
    treatment = models.TextField(default=None, null=True, blank=True)
    url = models.URLField(default=None, null=True, blank=True)


class MentalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'general_information', 'symptoms', 'prevention', 'treatment')


admin.site.register(MentalInfo, MentalInfoAdmin)
