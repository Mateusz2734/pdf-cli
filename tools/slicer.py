import os
import sys
sys.path.append('../functions')

from pypdf import PdfReader, PdfWriter

from tools.toolABC import Tool
from functions.slicetools import create_pageranges


class Slicer(Tool):
    def __init__(self, path: str, slices: str) -> None:
        self.execute(path, slices)

    def execute(self, path: str, slices: str):
        """
        It takes a PDF file and a list of page ranges, and writes a new PDF file with only the pages in
        the ranges

        :param path: Path to the PDF file
        :type path: str
        :param slices: The page ranges to extract
        :type slices: str
        """
        DESKTOP = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        filename = os.path.basename(path).split(".")[0]
        out = os.path.join(DESKTOP, f"{filename}-sliced.pdf")

        slices = create_pageranges(slices)

        writer = PdfWriter()
        reader = PdfReader(path)

        for slice in slices:
            writer.append(fileobj=reader, pages=slice)

        with open(out, "wb") as file:
            writer.write(file)
