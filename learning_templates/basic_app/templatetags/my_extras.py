from django import template

register = template.Library()

@register.filter(name='cut')
# value = the key in the context dictionary, arg = additional argument.
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut', cut)
