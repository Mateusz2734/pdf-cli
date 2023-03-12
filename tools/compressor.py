import os

from pypdf import PdfReader, PdfWriter

from tools.toolABC import Tool


class Compressor(Tool):
    def __init__(self, path: str, no_suffix: bool) -> None:
        self.suffix = "-compressed"
        if no_suffix:
            self.suffix = ""

        self.execute(path, self.suffix)

    def execute(self, path: str, suffix: str):
        """
        It takes a PDF file, reads it, compresses the content streams, and writes the compressed PDF to
        the desktop

        :param path: The path to the PDF file you want to compress
        """
        DESKTOP = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        filename = os.path.basename(path).split(".")[0]
        out = os.path.join(DESKTOP, f"{filename}{suffix}.pdf")

        reader = PdfReader(path)
        writer = PdfWriter()

        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)

        with open(out, "wb") as file:
            writer.write(file)
