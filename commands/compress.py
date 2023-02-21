import click
from pypdf.errors import PdfReadError
from tools.compressor import Compressor

@click.command(short_help="Compress pages of PDF")
@click.argument('path', nargs=1, metavar='<path>')
def compress(path):
    """
    This command takes <path> to PDF files, compressess its pages and saves new file on Desktop
    
    <path> is path to the PDF file you want to compress
    """
    try:
        compressor = Compressor(path)
    except IndexError:
        click.secho('ERROR: No file specified', err=True, fg="red")
    except FileNotFoundError:
        click.secho("ERROR: File does not exist", err=True, fg="red")
    except PdfReadError:
        click.secho("ERROR: File is not valid PDF", err=True, fg="red")
    else:
        click.secho("File compressed successfully", fg="green")