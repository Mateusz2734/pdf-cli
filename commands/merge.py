import click
from pypdf.errors import PdfReadError
from tools.merger import Merger


@click.command(short_help="Merge two or more PDFs")
@click.argument('paths', nargs=-1, metavar="<paths>")
@click.option("-s", "--no-suffix", is_flag=True, show_default=True, default=False, help="Do not add the '-merged' suffix")
def merge(paths, no_suffix):
    """
    This command takes <paths> to PDF files, merges them into one file and saves new file on Desktop

    <paths> are paths to the PDF files you want to merge
    """
    try:
        merger = Merger(paths, no_suffix)
    except IndexError:
        click.secho('ERROR: No files specified', err=True, fg="red")
    except FileNotFoundError:
        click.secho("ERROR: File does not exist", err=True, fg="red")
    except PdfReadError:
        click.secho("ERROR: File is not valid PDF", err=True, fg="red")
    else:
        click.secho("Files merged successfully", fg="green")
