import datetime

from django import template
from django.utils import timezone
import datetime
import pytz

utc=pytz.UTC

register = template.Library()


def convert_to_seconds(goal):
    percent_complete = 100
    start_time = goal.created.replace(tzinfo=utc)
    end_time = goal.due.replace(tzinfo=utc)
    if timezone.now() <= end_time:
        percent_complete = (timezone.now() - start_time) / (end_time - start_time) * 100
    return round(percent_complete, 2)


register.filter(convert_to_seconds)
