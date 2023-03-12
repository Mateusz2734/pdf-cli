import click
from pypdf.errors import PdfReadError
from tools.compressor import Compressor

@click.command(short_help="Compress pages of PDF")
@click.argument('path', nargs=1, metavar='<path>')
@click.option("-s", "--no-suffix", is_flag=True, show_default=True, default=False, help="Do not add the '-compressed' suffix")
def compress(path, no_suffix):
    """
    This command takes <path> to PDF files, compressess its pages and saves new file on Desktop
    
    <path> is path to the PDF file you want to compress
    """
    try:
        compressor = Compressor(path, no_suffix)
    except IndexError:
        click.secho('ERROR: No file specified', err=True, fg="red")
    except FileNotFoundError:
        click.secho("ERROR: File does not exist", err=True, fg="red")
    except PdfReadError:
        click.secho("ERROR: File is not valid PDF", err=True, fg="red")
    else:
        click.secho("File compressed successfully", fg="green")