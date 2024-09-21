from django import template
from packed import Elem, Component, psx_import

register = template.Library()

@register.simple_tag
def psx_syntax():

    psx_file_path = '/Users/coryfitz/Desktop/Framework/packed-test/mysite/myapp/templatetags/psx_main.psx'

    psx_syntax = psx_import(psx_file_path, 'psx_syntax')

    return psx_syntax()