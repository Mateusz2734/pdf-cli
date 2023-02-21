import click
from pypdf.errors import PdfReadError
from tools.merger import Merger


@click.command()
@click.argument('paths', nargs=-1)
def merge(paths):
    try:
        merger = Merger(paths)
    except IndexError:
        click.secho('ERROR: No files specified', err=True, fg="red")
    except FileNotFoundError:
        click.secho("ERROR: File does not exist", err=True, fg="red")
    except PdfReadError:
        click.secho("ERROR: File is not valid PDF", err=True, fg="red")
    else:
        click.secho("Files merged successfully", fg="green")
