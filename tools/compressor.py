import os

from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError

from toolABC import Tool


class Compressor(Tool):
    def __init__(self, path):
        self.execute(path)

    def execute(self, path):
        try:
            DESKTOP = os.path.join(os.path.join(
                os.environ['USERPROFILE']), 'Desktop')
            filename = os.path.basename(path).split(".")[0]
            out = os.path.join(DESKTOP, f"{filename}-compressed.pdf")

            reader = PdfReader(path)
            writer = PdfWriter()

            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)

            with open(out, "wb") as file:
                writer.write(file)

        except FileNotFoundError:
            print(f"File {path} does not exist")

        except PdfReadError:
            print(f"File {path} is not valid PDF")
