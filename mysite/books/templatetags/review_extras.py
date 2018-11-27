from django import template

register = template.Library()

def cut(value,args):
    return value.replace(args,'')

def lower(value):
    return value.lower()

register.filter('cut',cut)

register.filter('lower',lower)