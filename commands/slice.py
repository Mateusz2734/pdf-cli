import click
from pypdf.errors import PdfReadError
from tools.slicer import Slicer


@click.command()
@click.argument('path', nargs=1)
@click.argument('slice', nargs=1)
def slice(path, slice):
    try:
        slicer = Slicer(path, slice)
    except IndexError:
        click.secho('ERROR: No files specified', err=True, fg="red")
    except FileNotFoundError:
        click.secho("ERROR: File does not exist", err=True, fg="red")
    except PdfReadError:
        click.secho("ERROR: File is not valid PDF", err=True, fg="red")
    except ValueError:
        click.secho("ERROR: Wrong order of arguments", err=True, fg="red")
    else:
        click.secho("Slices extracted successfully", fg="green")