import click

from tools.merger import Merger


@click.command()
@click.argument('paths', nargs=-1)
def merge(paths):
    try:
        merger = Merger(paths)
    except IndexError:
        click.secho('ERROR: No files specified', err=True, fg="red")
