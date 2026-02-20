from django.contrib import admin
from django.db import models


class Contact(models.Model):
    class Meta:
        db_table = 'contact'
        get_latest_by = 'created'

    name = models.CharField(max_length=256, default=None, null=True, blank=True)
    email = models.EmailField(max_length=256, default=None, null=True, blank=True)
    feedback = models.TextField()


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback')


admin.site.register(Contact, ContactAdmin)
