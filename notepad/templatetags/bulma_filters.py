from django import template

register = template.Library()

@register.filter
def bulma_label(value, arg=None):
    if arg is None:
        arg = ""

    attrs = {
        'class': 'label ' + arg
    }
    return value.label_tag(label_suffix="", attrs=attrs)

@register.filter
def bulma_input(value, arg=None):
    if arg is None:
        arg = ""

    value.field.widget.attrs.update({ 'class': 'input ' + arg })
    return value

@register.filter
def bulma_textarea(value, arg=None):
    if arg is None:
        arg = ""

    value.field.widget.attrs.update({ 'class': 'textarea ' + arg })
    return value
