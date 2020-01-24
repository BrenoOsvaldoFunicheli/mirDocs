from django import template

register = template.Library()


@register.filter
def filter_components(component, topic):
    """Removes all values of arg from the given string"""
    return component == topic
