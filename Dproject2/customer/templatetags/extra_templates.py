from django import template

register =  template.Library()


@register.filter
def check_instance(data):

    return isinstance(data, dict)
