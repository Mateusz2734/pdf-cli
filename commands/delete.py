import click
from pypdf.errors import PdfReadError
from tools.deleter import Deleter


@click.command()
@click.argument('path', nargs=1)
@click.argument('slice', nargs=1)
def delete(path, slice):
    try:
        deleter = Deleter(path, slice)
    except IndexError:
        click.secho('ERROR: No files specified', err=True, fg="red")
    except FileNotFoundError:
        click.secho("ERROR: File does not exist", err=True, fg="red")
    except PdfReadError:
        click.secho("ERROR: File is not valid PDF", err=True, fg="red")
    else:
        click.secho("Slices deleted successfully", fg="green")