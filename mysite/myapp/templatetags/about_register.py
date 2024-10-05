from pathlib import Path
from django.conf import settings
from django import template
from packed import Elem, Component, psx_import

register = template.Library()

@register.simple_tag
def about_psx():

    psx_file_path = Path(settings.BASE_DIR) / 'myapp' / 'templatetags' / 'about.psx'

    about_psx = psx_import(psx_file_path, 'about_psx')

    return about_psx()