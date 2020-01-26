from django import template

register = template.Library()


@register.filter
def filter_components(component, section):
    return component.name == section.name


@register.filter
def html_type(component):
    pass


@register.filter
def is_paragraph(component, type_comp):
    if component.type_ref.name == 'Paragraph':
        if component.section.name == type_comp.name:
            print('passou com ' + component.section.name)
            return True
    return False


@register.filter
def is_header(component, type_comp):
    if component.type_ref.name == 'Header':
        if component.section.name == type_comp.name:
            return True
    return False


@register.filter
def is_figure(component, type):
    return type == 'fig'
