from django.contrib import admin
from django.db import models


class PhysicalInfo(models.Model):
    class Meta:
        db_table = 'physical_info'
        get_latest_by = 'created'

    name = models.CharField(max_length=256, default=None, null=True, blank=True)
    general_information = models.TextField(default=None, null=True, blank=True)
    symptoms = models.TextField(default=None, null=True, blank=True)
    diagnosis = models.TextField(default=None, null=True, blank=True)
    cause = models.TextField(default=None, null=True, blank=True)
    prevention = models.TextField(default=None, null=True, blank=True)
    treatment = models.TextField(default=None, null=True, blank=True)
    url = models.URLField(default=None, null=True, blank=True)


class PhysicalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'general_information', 'symptoms', 'diagnosis', 'cause', 'prevention', 'treatment', 'url')


admin.site.register(PhysicalInfo, PhysicalInfoAdmin)
