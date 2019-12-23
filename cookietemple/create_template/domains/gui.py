import os
import click
import cookietemple.create_template.create as create

WD = os.path.dirname(__file__)
TEMPLATES_PATH = f"{WD}/../templates"


@click.command()
@click.option('--language',
              type=click.Choice(['C++', 'C#', 'Java'], case_sensitive=False),
              prompt="Choose between the following options:")
def handle_gui(language):
    create.TEMPLATE_STRUCT["language"] = language
    print(create.TEMPLATE_STRUCT)
