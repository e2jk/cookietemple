import os
import sys
import click

from pathlib import Path
from ruamel.yaml import YAML
from cookietemple.util.dict_util import delete_keys_from_dict

WD = os.path.dirname(__file__)
TEMPLATES_PATH = f"{WD}/../create_template/templates"


@click.command()
def list_all():
    available_templates = load_available_templates()
    # listing does not need to display the long descriptions of the templates
    # users should use info for long descriptions
    delete_keys_from_dict(available_templates, ['long description'])

    click.echo(click.style('Run cookietemple info for long descriptions of your template of interest.', fg='green'))
    click.echo(click.style('All available templates:\n', fg='green'))

    yaml = YAML()
    yaml.dump(available_templates, sys.stdout)


def load_available_templates():
    path = Path(f"{TEMPLATES_PATH}/available_templates.yaml")
    yaml = YAML(typ='safe')
    return yaml.load(path)
