from pathlib import Path
from django.conf import settings
from django import template
from packed import Elem, Component, psx_import, packed

register = template.Library()

@register.simple_tag
@packed
def psx_syntax():

    psx_file_path = Path(settings.BASE_DIR) / 'myapp' / 'components' / 'psx_components.psx'
    
    main = psx_import(psx_file_path, 'main')

    return main()