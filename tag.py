from django import template

register = template.Library()


@register.filter
def sum_dic(dic, key):
    summation = 0
    for row in dic:
        if '.' in key:
            item = row[key.split('.')[0]][int(key.split('.')[1])]
        else:
            item = row[key]
        summation = summation + item
    return summation


@register.simple_tag()
def divide(value, divider):
    return value / divider
