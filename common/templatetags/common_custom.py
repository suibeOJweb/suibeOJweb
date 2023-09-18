from django import template

register = template.Library()


@register.filter
def div(value, d):
    if d == 0 :
        return 0
    return round((value / d * 100), 2)
