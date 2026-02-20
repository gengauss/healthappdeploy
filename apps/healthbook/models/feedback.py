from django.contrib import admin
from django.db import models
from import_export.admin import ImportExportModelAdmin

CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


USING_CHOICES = (
    ("1日以下", "1日以下"),
    ("3日間", "3日間"),
    ("1週間以内", "1週間以内"),
    ("2週間以内", "2週間以内"),
    ("1ヵ月以上", "1ヵ月以上"),
)


class Feedback(models.Model):
    class Meta:
        db_table = 'feedback'
        get_latest_by = 'created'

    # healthbook
    hb_content = models.CharField(max_length=6, choices=CHOICES, default='None')
    hb_design = models.CharField(max_length=6, choices=CHOICES, default='None')
    hb_change = models.CharField(max_length=6, choices=CHOICES, default='None')
    hb_feedback = models.TextField(null=True, blank=True)

    # visualization
    vs_content = models.CharField(max_length=6, choices=CHOICES, default='None')
    vs_design = models.CharField(max_length=6, choices=CHOICES, default='None')
    vs_change = models.CharField(max_length=6, choices=CHOICES, default='None')
    vs_feedback = models.TextField(null=True, blank=True)

    # healthtracker
    fr_design = models.CharField(max_length=6, choices=CHOICES, default='None')
    fr_use = models.CharField(max_length=6, choices=USING_CHOICES, default='None')
    fr_opinion = models.TextField(null=True, blank=True)
    fr_change = models.CharField(max_length=6, choices=CHOICES, default='None')
    fr_feedback = models.TextField(null=True, blank=True)

    ct_design = models.CharField(max_length=6, choices=CHOICES, default='None')
    ct_use = models.CharField(max_length=6, choices=USING_CHOICES, default='None')
    ct_opinion = models.TextField(null=True, blank=True)
    ct_change = models.CharField(max_length=6, choices=CHOICES, default='None')
    ct_feedback = models.TextField(null=True, blank=True)

    hg_design = models.CharField(max_length=6, choices=CHOICES, default='None')
    hg_use = models.CharField(max_length=6, choices=USING_CHOICES, default='None')
    hg_opinion = models.TextField(null=True, blank=True)
    hg_change = models.CharField(max_length=6, choices=CHOICES, default='None')
    hg_feedback = models.TextField(null=True, blank=True)


class FeedbackAdmin(ImportExportModelAdmin):
    list_display = ('hb_content', 'hb_design', 'hb_change', 'hb_feedback',
                    'vs_content', 'vs_design', 'vs_change', 'vs_feedback',
                    'fr_design', 'fr_use', 'fr_opinion', 'fr_change', 'fr_feedback',
                    'ct_design', 'ct_use', 'ct_opinion', 'ct_change', 'ct_feedback',
                    'hg_design', 'hg_use', 'hg_opinion', 'hg_change', 'hg_feedback')


admin.site.register(Feedback, FeedbackAdmin)
