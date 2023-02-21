import click
from pypdf.errors import PdfReadError
from tools.deleter import Deleter


@click.command(short_help="Delete pages from PDF")
@click.argument('path', nargs=1, metavar="<path>")
@click.argument('slice', nargs=1, metavar="<slice>")
def delete(path, slice):
    """
    This command takes <path> to PDF file, deletes <slice> of pages and saves new file on Desktop
    
    <path> is path to the PDF file

    <slice> is string of ranges, eg. '1,3,7:18' that will not be in the new file.
    NOTE that first page is 1, not 0 
    """
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