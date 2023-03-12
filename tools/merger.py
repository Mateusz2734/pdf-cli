from typing import List
import os

from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError

from tools.toolABC import Tool


class Merger(Tool):
    def __init__(self, paths: List[str], no_suffix: bool) -> None:
        self.suffix = "-merged"
        if no_suffix:
            self.suffix = ""

        self.execute(paths, self.suffix)

    def execute(self, paths: List[str], suffix: str):
        """
        It takes a list of paths to PDF files, merges them into a single PDF file, and saves the merged
        PDF file to the desktop

        :param paths: A list of paths to the PDFs you want to merge
        :type paths: List[str]
        """

        DESKTOP = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        filename = os.path.basename(paths[0]).split(".")[0]
        out = os.path.join(DESKTOP, f"{filename}{suffix}.pdf")

        writer = PdfWriter()

        for path in paths:
            self.add_to_writer(path, writer)

        with open(out, "wb") as file:
            writer.write(file)

    def add_to_writer(self, path: str, writer: PdfWriter):
        """
        It takes a path to a PDF file, and a PdfWriter object, and adds the pages of the PDF file to the
        PdfWriter object

        :param path: str - the path to the PDF file
        :type path: str
        :param writer: PdfWriter
        :type writer: PdfWriter
        """
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
