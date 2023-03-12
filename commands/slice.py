import click
from pypdf.errors import PdfReadError
from tools.slicer import Slicer


@click.command(short_help="Extract pages from PDF")
@click.argument('path', nargs=1, metavar="<path>")
@click.argument('slice', nargs=1, metavar="<slice>")
@click.option("-s", "--no-suffix", is_flag=True, show_default=True, default=False, help="Do not add the '-sliced' suffix")
def slice(path, slice, no_suffix):
    """
    This command takes <path> to PDF file, extracts <slice> of pages and saves new file on Desktop
    
    <path> is path to the PDF file

    <slice> is string of ranges, eg. '1,3,7:18' that be in the new file.
    NOTE that first page is 1, not 0 
    """
    try:
        slicer = Slicer(path, slice, no_suffix)
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