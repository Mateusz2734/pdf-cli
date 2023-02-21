import click

from commands.merge import merge
from commands.compress import compress
from commands.delete import delete
from commands.slice import slice

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Group of commands to manipulate PDF files"""
    pass


cli.add_command(merge)
cli.add_command(compress)
cli.add_command(delete)
cli.add_command(slice)