from pathlib import Path
from django.conf import settings
from django import template
from packed import Elem, Component, psx_import

register = template.Library()

@register.simple_tag
def psx_syntax():

    psx_file_path = Path(settings.BASE_DIR) / 'myapp' / 'templatetags' / 'psx_main.psx'

    psx_syntax = psx_import(psx_file_path, 'psx_syntax')

    return psx_syntax()