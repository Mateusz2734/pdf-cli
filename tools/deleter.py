from tools.toolABC import Tool
from functions.slicetools import create_pageranges, invert_slices
from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError
from typing import List
import os
import sys
sys.path.append('../functions')


class Deleter(Tool):
    def __init__(self, path: str, slices: str, no_suffix: bool) -> None:
        self.suffix = "-deleted"
        if no_suffix:
            self.suffix = ""

        self.execute(path, slices, self.suffix)

    def execute(self, path: str, slices: str, suffix: str):
        """
        It takes a PDF file and a string of page ranges, and returns a new PDF file with the pages in
        the ranges removed

        :param path: Path to the PDF file
        :type path: str
        :param slices: The pages to delete, a string of page ranges, e.g. "1-3,5,7-9"
        :type slices: str
        """
        DESKTOP = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        filename = os.path.basename(path).split(".")[0]
        out = os.path.join(DESKTOP, f"{filename}{suffix}.pdf")

        writer = PdfWriter()
        reader = PdfReader(path)

        slices = create_pageranges(invert_slices(slices, len(reader.pages)))

        for slice in slices:
            writer.append(fileobj=reader, pages=slice)

        with open(out, "wb") as file:
            writer.write(file)
