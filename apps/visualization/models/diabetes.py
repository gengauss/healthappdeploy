from django.contrib import admin
from django.db import models


class Diabetes(models.Model):
    class Meta:
        db_table = 'diabetes'
        get_latest_by = 'created'

    preg = models.IntegerField()
    plas = models.IntegerField()
    pres = models.IntegerField()
    skin = models.IntegerField()
    insu = models.IntegerField()
    mass = models.FloatField()
    pedi = models.FloatField()
    age = models.IntegerField()
    tested = models.CharField(max_length=50)


class DiabetesAdmin(admin.ModelAdmin):
    list_display = ('preg', 'plas', 'pres', 'skin', 'insu', 'mass', 'pedi', 'age', 'tested')


admin.site.register(Diabetes, DiabetesAdmin)
