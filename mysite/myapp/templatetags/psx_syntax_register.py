from pathlib import Path
from django.conf import settings
from django import template
from psx_syntax import psx_import, packed

register = template.Library()

# Define the base path where the PSX files are located
psx_dir_path = Path(settings.BASE_DIR) / 'myapp' / 'components'

# Iterate over each .psx file in the directory
for psx_file in psx_dir_path.glob('*.psx'):
    # Extract the file stem (filename without extension)
    component_name = psx_file.stem

    # Define a dynamic function for each component found
    def create_psx_tag(psx_file_path, component_name):
        @register.simple_tag(name=component_name)
        @packed
        def component_tag():
            # Dynamically import the PSX file and call the appropriate component
            main = psx_import(psx_file_path, component_name)
            return main()

        return component_tag

    # Call the function to create and register the template tag
    create_psx_tag(psx_file, component_name)
