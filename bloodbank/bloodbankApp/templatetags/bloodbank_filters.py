from django import template

register = template.Library()

@register.filter(name='get_primary_key')
def get_primary_key(arg, dict):
    data_list = list(dict.values())
    pk = data_list[0]
    return pk
