from django import template
import datetime
register = template.Library()

def get_current_date():
    return datetime.datetime.now()

register.assignment_tag(get_current_date)