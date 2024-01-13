from django import template
register=template.Library()


def swap(value):
     return value.swapcase()
register.filter('swapping',swap)

@register.filter()
def remove(value,arg):
     return value.replace(arg,'')

