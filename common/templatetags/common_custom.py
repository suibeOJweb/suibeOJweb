from django import template

register = template.Library()


@register.filter
def div(value, d):
    return round((value / d * 100), 2)
