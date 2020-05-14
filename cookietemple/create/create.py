import click

from cookietemple.create.domains.CliCreator import CliCreator
from cookietemple.create.domains.WebCreator import WebCreator
from cookietemple.create.domains.GuiCreator import GuiCreator
from cookietemple.create.domains.PubCreator import PubCreator


def choose_domain(domain: str):
    """
    Prompts the user for the template domain.
    Creates the .cookietemple file.
    Prompts the user whether or not to create a Github repository

    :param domain: Template domain
    """

    if not domain:
        domain = click.prompt('Choose between the following domains [cli, gui, web, pub]',
                              type=click.Choice(['cli', 'gui', 'web', 'pub']))

    switcher = {
        'cli': CliCreator,
        'web': WebCreator,
        'gui': GuiCreator,
        'pub': PubCreator
    }

    creator_obj = switcher.get(domain.lower(), lambda: 'Invalid domain!')()
    creator_obj.create_template()
