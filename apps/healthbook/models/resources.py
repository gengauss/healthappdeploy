from django.contrib import admin
from django.db import models
from import_export import resources
from apps.healthbook.models.feedback import Feedback
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


class FeedbackResource(resources.ModelResource):
    class Meta:
        models = Feedback


class FeedbackAdmin(ImportExportModelAdmin):
    list_display = ('hb_content', 'hb_design', 'hb_change', 'hb_feedback',
                    'vs_content', 'vs_design', 'vs_change', 'vs_feedback',
                    'fr_design', 'fr_use', 'fr_opinion', 'fr_change', 'fr_feedback',
                    'ct_design', 'ct_use', 'ct_opinion', 'ct_change', 'ct_feedback',
                    'hg_design', 'hg_use', 'hg_opinion', 'hg_change', 'hg_feedback')
    pass
